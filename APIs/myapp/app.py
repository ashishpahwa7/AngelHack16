from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Person, Patient
import os

engine = create_engine('sqlite:///patient.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__) 


#Make an app.route() decorator here
@app.route("/")
@app.route("/get_records", methods = ['GET', 'POST'])
def awsomeFunction():
  if request.method == 'GET':
    #Call the method to Get all of the records
    return getAllRecords()
  elif request.method == 'POST':
    #Call the method to make create a new record
    name = request.args.get('name', '')
    gender = request.args.get('gender', '')
    address = request.args.get('address', '')
    ID = request.args.get('id', '')

    return creatUser(name, gender, address, ID)
    
    #Create new patient record here : #TODO

@app.route("/get_user/<int:id>", methods = ['GET', 'PUT', 'DELETE'])
def awsomeFunctionID(id):

  if request.method == 'GET':
    return getUser(id)  #method to view detail of specific user

  elif request.method == 'PUT':
    name = request.args.get('name', '')
    ID = request.args.get('id', '')
    gender = request.args.get('gender','')
    address=request.args.get('address','')
    #return updateUser(name.ID,address,gender) #method to edit user details :TODO


## After lot of code loss starting coding the new modules from here :

@app.route("/user_login",methods=['POST'])
def user_login():

  ID = request.args.get('uid','')

  if request.method== 'POST':
    return getUser(ID)


# adding this route and method just to add new UID holders to database , no practical purpose for this project otherqwise
@app.route("/create_user", methods=['POST'])
def create_user():

  uid = request.args.get('uid','')
  name = request.args.get('name','')
  adress = request.args.get('adress','')
  gender = request.args.get('gender','')
  age = request.args.get('age','')
  dob = request.args.get('dob','')  

  if request.method == 'POST':
    return creatUser(uid, name, adress, gender, age, dob)


@app.route("/get_patient", methods=['POST'])
def get_patient():

  ID = request.args.get('uid','')

  if request.method=='POST':
    return getPatient(ID)

@app.route("/modify_patient/<int:uid>", methods=['GET','PUT','DELETE'])
def modify_patient(uid):
  
  height = request.args.get('height', '')
  weight = request.args.get('weight','')

  if request.method == 'GET':
    return getPatient(uid)

  elif request.method =='PUT':
    return updatePatient(uid, height, weight)

  elif request.method =='DELETE':
     return deletePatient(uid)


@app.route("/create_patient", methods=['POST'])
def create_patient():
  
  height = request.args.get('height', '')
  weight = request.args.get('weight','')
  uid = request.args.get('uid','')
  file_number=request.args.get('file','')
  date = request.args.get('date','')


  if request.method=='POST':
    return createPatient(uid,height,weight,file_number,date)


''' 
def getAllRecords():
  data = session.query(Patient).all()
  return jsonify(Data=[i.serialize for i in data])
'''
  
def creatUser(uid, name, adress, gender, age, dob):
 
  data = Person(uid = uid, adress=adress, gender=gender, age=age, dob=dob, name=name)
  session.add(data)
  session.commit()

  return "Success"


def getUser(id):
  data = session.query(Person).filter_by(uid = id).one()
  return jsonify(data=data.serialize)


def createPatient(uid,date,height,weight,file_number):
  data = Patient(uid=uid, height=height, weight=weight, file_number=file_number)
  session.add(data)
  session.commit()
  return "Success"


def getPatient(id):
  
  data = session.query(Patient).filter_by(uid = id).one()
  return jsonify(data=data.serialize) 

def updatePatient(uid, height, weight):
  data = session.query(Patient).filter_by(uid = uid).one()
  data.height = height
  data.weight = weight
  
  session.add(data)
  session.commit()
  
  return "Updated a Patient with file number %s" % uid

def deletePatient(uid):
  puppy = session.query(Patient).filter_by(uid = uid).one()
  session.delete(puppy)
  session.commit()
  return "Removed Puppy with id %s" % uid


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  