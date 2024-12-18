from sqlalchemy import Column, Integer, String
from database.db_setup import SessionLocal,Base
from sqlalchemy.orm import sessionmaker

session = SessionLocal()

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)

# CRUD Functions
def create_doctor(name, specialty):
    session = SessionLocal()
    try:
        doctor = Doctor(name=name, specialty=specialty)
        session.add(doctor)
        session.commit()
        print("Doctor added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

def get_doctors():
    session = SessionLocal()
    try:
        doctors = session.query(Doctor).all()  # Querying all doctors from the database
        if not doctors:  # If no doctors are found, notify the user
            print("No doctors found.")
        else:
            print("\nList of Doctors:")
            for doctor in doctors:
                print(f"ID: {doctor.id}, Name: {doctor.name}, Specialty: {doctor.specialty}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def update_doctor(doctor_id, name=None, specialty=None):
    session = SessionLocal()
    try:
        doctor = session.query(Doctor).get(doctor_id)
        if not doctor:
            print(f"No doctor found with ID {doctor_id}")
            return False
        
        if name:
            doctor.name = name
        if specialty:
            doctor.specialty = specialty

        session.commit()
        print("Doctor updated successfully!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        session.close()

def delete_doctor(doctor_id):
    session = SessionLocal()
    try:
        doctor = session.query(Doctor).get(doctor_id)
        if doctor:
            session.delete(doctor)
            session.commit()
            print("Doctor deleted successfully!")
        else:
            print(f"No doctor found with ID {doctor_id}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
