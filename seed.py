from models import db, Pet
from app import app

db.drop_all()
db.create_all()

dexter = Pet(name="Dexter",species="dog",photo_url="https://www.mygavet.com/sites/default/files/styles/large/public/dalmatian-dog-breed-info.jpg?itok=maaJf_Lk", age=3, notes="Will do anything for a kibble", available=False)

koda = Pet(name="Koda", species="cat", photo_url="https://previews.123rf.com/images/milanbojanic/milanbojanic1709/milanbojanic170900002/85452647-a-yellow-cat-with-blue-eyes-looking-straight.jpg",notes="Will claw you if you play the song 'Sweet Caroline',")

piney = Pet(name="Piney", species="porcupine", photo_url="https://img.buzzfeed.com/buzzfeed-static/static/2014-06/26/19/campaign_images/webdr10/this-baby-porcupine-makes-the-cutest-noise-when-i-2-31113-1403823990-0_dblbig.jpg", age=7)

db.session.add_all([dexter,koda,piney])
db.session.commit()