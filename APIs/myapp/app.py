from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Patient
import os

engine = create_engine('sqlite:///patient.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__) 

# Create the appropriate app.route functions, 
#test and see if they work



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



  
def getAllRecords():
  data = session.query(Patient).all()
  return jsonify(Data=[i.serialize for i in data])

  
def creatUser(name, gender, address, ID):
  data = Patient(name = name, gender = gender, address=address, id=ID, file_number=97)
  session.add(data)
  session.commit()
  return "Success"


def getUser(id):
  data = session.query(Patient).filter_by(id = id).one()
  return jsonify(data=data.serialize)

    

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  