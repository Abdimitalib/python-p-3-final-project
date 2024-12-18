import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.doctor import create_doctor, get_doctors, update_doctor, delete_doctor
from models.patient import create_patient, get_patients, update_patient, delete_patient
from models.appointment import create_appointment, get_appointments, update_appointment, delete_appointment
from database.db_setup import init_db

# Welcome message
def welcome():
    print("Welcome to the Hospital Management System")

# Main menu options
def show_menu():
    print("\nChoose an option:")
    print("1. Manage Doctors")
    print("2. Manage Patients")
    print("3. Manage Appointments")
    print("4. Exit")

# Manage Doctors submenu
def manage_doctors():
    while True:
        print("\nManage Doctors:")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter doctor's name: ")
            specialty = input("Enter doctor's specialty: ")
            create_doctor(name, specialty)
        elif choice == '2':
            get_doctors()  
        elif choice == '3':
            doctor_id = int(input("Enter doctor ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            specialty = input("Enter new specialty (leave blank to keep current): ")
            update_doctor(doctor_id, name, specialty)
        elif choice == '4':
            doctor_id = int(input("Enter doctor ID to delete: "))
            delete_doctor(doctor_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Manage Patients submenu
def manage_patients():
    while True:
        print("\nManage Patients:")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            create_patient()
        elif choice == '2':
            get_patients()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_appointments():
    while True:
        print("\nManage Appointments:")
        print("1. Add Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            reason = input("Enter reason for appointment: ")
            date_time_str = input("Enter appointment date and time (YYYY-MM-DD HH:MM:SS): ")
            patient_id = int(input("Enter patient ID: "))
            create_appointment(reason, date_time_str, patient_id)
        elif choice == '2':
            get_appointments()
        elif choice == '3':
            appointment_id = int(input("Enter appointment ID to update: "))
            reason = input("Enter new reason (leave blank to keep current): ")
            date_time_str = input("Enter new appointment date and time (YYYY-MM-DD HH:MM:SS) or leave blank: ")
            patient_id = input("Enter new patient ID (leave blank to keep current): ")

            if not reason:
                reason = None
            if not date_time_str:
                date_time_str = None
            if not patient_id:
                patient_id = None
            else:
                patient_id = int(patient_id)

            update_appointment(appointment_id, reason, date_time_str, patient_id)
        elif choice == '4':
            appointment_id = int(input("Enter appointment ID to delete: "))
            delete_appointment(appointment_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    init_db()  # Initialize the database

    welcome()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_doctors()
        elif choice == '2':
            manage_patients()
        elif choice == '3':
            manage_appointments()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
