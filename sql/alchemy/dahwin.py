from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    ssn = Column('ssn',Integer,primary_key=True)
    firstname = Column('firstname',String)
    lastname = Column('lasname',String)
    gender = Column('gender',CHAR)
    age = Column('age',Integer)


    def __init__(self,ssn,first,last,gender,age):
        super().__init__()
        self.ssn = ssn
        self.first = first
        self.last = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn}),({self.firstname}),({self.lastname}),({self.gender}),({self.age})"

engine = create_engine('sqlite:///dahwin.db', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

person = Person(777666333,'Dahyun','Darwin','dahwin',25)
session.add(person)
session.commit()
