## Hospital Management System
In this challenge, we will be working with a Hospital domain. We have three models: Patient, Doctor, and Appointment.

For our purposes:

A Doctor can have many Appointments, and a Patient can have many Appointments.
An Appointment belongs to both a Doctor and a Patient.
# Relationships:
Doctor - Patient is a many-to-many relationship, meaning a Doctor can see multiple Patients and a Patient can visit multiple Doctors.
Appointment is a junction table between Doctor and Patient to represent the many-to-many relationship.
Folder Structure
app.py - The main entry point for testing your code.
database/ - Contains files for database connection and setup.
setup.py - Defines SQL queries to create the database tables.
connection.py - Handles database connection strings.
models/ - Contains the models (Patient.py, Doctor.py, Appointment.py) where you will define your CRUD methods.
tests/ - Contains test cases to validate your code.
Core Deliverables
You need to implement the following methods for the models Patient, Doctor, and Appointment. Use the methods described below for interacting with the database.

## Initializers and Properties
# Patient
Patient __init__(self, id, name, age, gender)
Initializes a new Patient object with a name, age, and gender.
This should create a new entry in the database patients table.
Patient property id
Returns the id of the newly created Patient.
The id must be an int type.
Patient property name
Returns the name of the patient.
Name must be of type str.
Names must be longer than 0 characters.
Should not be able to change after the patient is instantiated.
Patient property age
Returns the patient's age.
Age must be an int and greater than 0.

# Doctor
Doctor __init__(self, id, name, specialty)
Initializes a new Doctor object with a name and specialty.
This should create a new entry in the doctors table.
Doctor property id
Returns the id of the newly created Doctor.
id must be of type int.
Doctor property name
Returns the doctor's name.
Name must be of type str.
Names must be longer than 0 characters.
Should not be able to change after the doctor is instantiated.
Doctor property specialty
Returns the doctor's specialty.
Specialty must be of type str.
# Appointment
Appointment __init__(self, doctor, patient, date_time)
Initializes a new Appointment object with a Doctor, a Patient, and a date_time.
This should create a new entry in the appointments table, using doctor_id and patient_id as foreign keys.
Appointment property date_time
Returns the appointment's date and time.
date_time must be of type str or datetime and in a valid date format.
Should not be able to change after the appointment is created.
Object Relationship Methods and Properties
Appointment
Appointment property doctor
Returns the doctor of the appointment.
This will make use of a SQL JOIN to fetch the doctor details based on the doctor_id.
Appointment property patient
Returns the patient of the appointment.
This will make use of a SQL JOIN to fetch the patient details based on the patient_id.
Doctor
Doctor appointments()
Returns a list of all Appointments associated with a Doctor.
Use SQL JOINS to fetch all appointments for the given doctor.
Doctor patients()
Returns a list of all Patients associated with a Doctor.
Use SQL JOINS to fetch all patients for the given doctor.
Patient
Patient appointments()

Returns a list of all Appointments associated with a Patient.
Use SQL JOINS to fetch all appointments for the given patient.
Patient doctors()

Returns a list of all Doctors associated with a Patient.
Use SQL JOINS to fetch all doctors for the given patient.
Aggregate and Association Methods
Doctor
Doctor patient_names()

Returns a list of names of all patients who have appointments with the doctor.
Returns None if the doctor has no appointments.
Doctor frequent_patients()

Returns a list of patients who have more than 2 appointments with the doctor.
Returns None if the doctor has no such patients.
Patient
Patient doctor_names()
Returns a list of names of all doctors that the patient has seen.
Returns None if the patient has no appointments.
## Folder Structure Details
app.py
The main entry point for testing your code and models. You will create instances of Doctor, Patient, and Appointment, and test the relationships and methods you’ve implemented.

models/
Doctor.py - Contains the Doctor model with methods like appointments(), patients(), etc.
Patient.py - Contains the Patient model with methods like appointments(), doctors(), etc.
Appointment.py - Contains the Appointment model with methods like doctor(), patient(), etc.
database/
setup.py - Write SQL queries here to create tables for patients, doctors, and appointments.
connection.py - Provides the database connection string for interacting with the database.

1. Install dependencies:

pipenv install
2. Enter the shell:

pipenv shell
3. Run the application to create the database:

python3 app.py