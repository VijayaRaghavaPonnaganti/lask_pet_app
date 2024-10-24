from app import db1, Pet 
#inserting some pets
petA = Pet(name="A",species="RAT", age=1)
petB = Pet(name="B",species="PANDA",age=7)
petC = Pet(name="C",species="CAT",age=4)

db1.session.add(petA)
db1.session.add(petB)
db1.session.add(petC)

db.session.commit()
