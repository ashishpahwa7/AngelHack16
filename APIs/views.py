from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Patient


engine = create_engine('sqlite:///patient.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__) 

# Create the appropriate app.route functions, 
#test and see if they work


#Make an app.route() decorator here
@app.route("/")
@app.route("/get_records/", methods = ['GET', 'POST'])
def puppiesFunction():
  if request.method == 'GET':
    #Call the method to Get all of the records
    return getAllRecords()
  elif request.method == 'POST':
    #Call the method to make create a new record
    print "Adding a New Patient Record"
    
    #Create new patient record here : #TODO
    
    return createANewRecord(args)
 
  
def getAllRecords():
  data = session.query(Patient).all()
  return jsonify(Data=[i.serialize for i in data])

  
def createANewRecord(args):
  data = Patient(name = name, description = description)
  session.add(data)
  session.commit()
  return jsonify(Patient=data.serialize)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)  
