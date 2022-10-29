import db
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db.engine)
session =Session()

for object in session.query(db.transactions).all():
    print(object.transaction_id, object.price)

print("Transactions with price over 40$:")

for object in session.query(db.transactions).filter(db.transactions.price > 40):
    print(object.transaction_id, object.price, object.bill_type)