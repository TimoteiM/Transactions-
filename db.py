from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
base = declarative_base()

class transactions(base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    date = Column(String)
    item_id = Column(Integer)
    price = Column(Integer)
    bill_type = Column(String)

    def __init__(self, transaction_id, date, item_id, price, bill_type):
        self.transaction_id = transaction_id
        self.date = date
        self.item_id = item_id
        self.price = price
        self.bill_type = bill_type

base.metadata.create_all(engine)