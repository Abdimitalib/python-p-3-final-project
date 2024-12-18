from sqlalchemy import Column, Integer, String
from database.db_setup import SessionLocal,Base

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    doctor_id = Column(Integer)

def create_patient():
    session = SessionLocal()
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    doctor_id = int(input("Enter doctor's ID: "))
    patient = Patient(name=name, age=age, doctor_id=doctor_id)
    session.add(patient)
    session.commit()
    session.close()
    print("Patient added successfully!")

def get_patients():
    session = SessionLocal()
    patients = session.query(Patient).all()
    for patient in patients:
        print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}")
    session.close()

def update_patient():
    session = SessionLocal()
    patient_id = int(input("Enter patient's ID to update: "))
    patient = session.query(Patient).filter(Patient.id == patient_id).first()
    
    if patient:
        patient.name = input("Enter new name: ")
        patient.age = int(input("Enter new age: "))
        session.commit()
        print("Patient updated successfully!")
    else:
        print("Patient not found.")
    
    session.close()

def delete_patient():
    session = SessionLocal()
    patient_id = int(input("Enter patient's ID to delete: "))
    patient = session.query(Patient).filter(Patient.id == patient_id).first()
    
    if patient:
        session.delete(patient)
        session.commit()
        print("Patient deleted successfully!")
    else:
        print("Patient not found.")
    
    session.close()
