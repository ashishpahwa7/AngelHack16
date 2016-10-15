from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from geocode import getGeocodeLocation

Base = declarative_base()


class Person(Base):
    __tablename__='person'
    
    name=Column(String(80),nullable=False)
    gender=Column(String(1),nullable=False)
    uid=Column(Integer,primary_key=True)
    adress=Column(String(250))
    age=Column(String(3),nullable=False)
    dob=Column(String(10),nullable=False)
    

    
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           
           'uid': self.uid,
           'name': self.name,
           'gender' : self.gender,
           'dob':self.dob,
           'address':self.adress,
           'age': self.age

       }


class Patient(Base):
    
    __tablename__ = 'patient'

    uid = Column(Integer, primary_key = True)
    date = Column(String(10),nullable=True)
    height = Column(Integer,nullable=False)
    weight= Column(Integer,nullable=False)
    file_number = Column(Integer,nullable=True)           
    
    def _init_():
    
        self.file_number=0
        self.uid=0
        self.height=0.0
        self.weight=0.0
        self.date="dd/mm/yyyy"

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           
           'uid': self.uid,
           'date': self.date,
           'height' : self.height,
           'weight':self.weight,
           'file_number':self.file_number

       }
 

class Insurance_Policy(Base):
    __tablename__ = 'Insurance_Policy'

    insurance_no = Column(Integer, primary_key = True)
    cost = Column(Integer,nullable=False)
    insurance_plan=Column(String(20),nullable=False)
    file_number = Column(Integer,nullable=True) 
    #insurance paper digital , id_card ,         
    
    def _init_():
        self.file_number=0
        self.insurance_no=0
        self.insurance_plan=''
        self.cost=0.0

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           
           'insurance_no': self.insurance_no,
           'insurance_plan': self.insurance_plan,
           'cost':self.cost,
           'file_number':self.file_number

       }



class HealthHistory(Base):

  file_number = Column(String(20),primary_key=True)
  # Features for predicting heart disease ( UCI machine learning repository)
  age = Column(Integer,nullable=True)
  sex = Column(String(1),nullable=True)
  cp = Column(String(),nullable=True) # chess pain type : -- Value 1: typical angina -- Value 2: atypical angina -- Value 3: non-anginal pain 
  trestbps = Column(String(3),nullable=True) # resting blood pressure on admision
  chol =Column(String(5),nullable=True) #serum cholestoral in mg/dl 
  fbs = Column(Integer,nullable=True)  #fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
  restecg = Column(Integer,nullable=True)   # resting electrocardiographic results
  thalach = Column(String(12),nullable=True)

'''
-- Value 0: normal 
-- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) 
-- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria  
'''
   #maximum heart rate achieved 
  excang =  Column(String(12),nullable=True) #exercise induced angina (1 = yes; 0 = no) 
  oldpeak = Column(String(5),nullable=True)  #ST depression induced by exercise relative to rest 
  slope = Column(String(10), nullable=True)

  #slope: the slope of the peak exercise ST segment
'''-- Value 1: upsloping 
-- Value 2: flat 
-- Value 3: downsloping  
''' 
  ca=  Column(String(12), nullable=True) #ca: number of major vessels (0-3) colored by flourosopy  
  thal = Column(Integer,nullable=True)    #thal: 3 = normal; 6 = fixed defect; 7 = reversable defec
  num = Column(Integer,nullable=True)



engine = create_engine('sqlite:///patient.db')
Base.metadata.create_all(engine)