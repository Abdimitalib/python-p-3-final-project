from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.db_setup import Base, SessionLocal
from datetime import datetime

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    reason = Column(String, nullable=False)
    date_time = Column(DateTime, default=datetime.now)  
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)

    patient = relationship("Patient", backref="appointments")


def create_appointment(reason: str, date_time: str, patient_id: int):
    session = SessionLocal()  
    try:
        appointment_date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        appointment = Appointment(reason=reason, date_time=appointment_date_time, patient_id=patient_id)
        session.add(appointment)
        session.commit()
        print("Appointment created successfully!")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
    finally:
        session.close()

def get_appointments():
    session = SessionLocal() 
    try:
        appointments = session.query(Appointment).all()
        for appointment in appointments:
            print(f"ID: {appointment.id}, Patient ID: {appointment.patient_id}, "
                  f"Reason: {appointment.reason}, DateTime: {appointment.date_time.strftime('%Y-%m-%d %H:%M:%S')}")
    finally:
        session.close()

def update_appointment(appointment_id: int, reason: str = None, date_time: str = None, patient_id: int = None):
    session = SessionLocal() 
    try:
        appointment = session.query(Appointment).get(appointment_id)
        if not appointment:
            print("Appointment not found.")
            return False
        if reason:
            appointment.reason = reason
        if date_time:
            try:
                appointment.date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
                return False
        if patient_id:
            appointment.patient_id = patient_id
        session.commit()
        print("Appointment updated successfully!")
        return True
    except Exception as e:
        print(f"Error updating appointment: {e}")
        return False
    finally:
        session.close()

def delete_appointment(appointment_id: int):
    session = SessionLocal() 
    try:
        appointment = session.query(Appointment).get(appointment_id)
        if appointment:
            session.delete(appointment)
            session.commit()
            print("Appointment deleted successfully!")
        else:
            print("Appointment not found.")
    except Exception as e:
        print(f"Error deleting appointment: {e}")
    finally:
        session.close()
