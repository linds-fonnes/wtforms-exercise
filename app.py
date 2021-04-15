from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SecretSecretSecret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def show_home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET","POST"])
def show_add_pet_form():
    """Renders form to add a new pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET","POST"])    
def show_pet_details(pet_id):
    """Shows details about a specific pet along with a form to edit some of their info"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f"/{pet.id}")

    return render_template("pet_details.html", pet=pet, form=form)