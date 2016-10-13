from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from geocode import getGeocodeLocation

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patient'


    name =Column(String(80), nullable = False)
    gender = Column(String(1),nullable=False)
    id = Column(Integer, primary_key = True)
    address = Column(String(250))
    file_number = Column(Integer,nullable=True)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'id': self.id,
           'name': self.name,
           'address' : self.address,
           'gender':self.gender,

       }
 

engine = create_engine('sqlite:///patient.db')
Base.metadata.create_all(engine)
