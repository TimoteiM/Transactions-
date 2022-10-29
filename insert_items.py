import db
from sqlalchemy.orm import sessionmaker
import random

Session = sessionmaker(bind=db.engine)
session = Session()

for object in range(1,11):
    item_id = random.randint(0,1000)
    price = random.randint(20,60)

    tr = db.transactions(object, "29/10/2022", item_id, price, "$")
    session.add(tr)

session.commit()
