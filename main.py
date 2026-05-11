import os

PATIENT_FILE = "patients.txt"
APPOINTMENT_FILE = "appointments.txt"
DOCTOR_FILE = "doctors.txt"

# =========================
# CREATE FILES IF NOT EXIST
# =========================

def create_files():
    files = [PATIENT_FILE, APPOINTMENT_FILE, DOCTOR_FILE]
    for file in files:
        if not os.path.exists(file):
            open(file, 'w').close()

# =========================
# ADD PATIENT
# =========================

def add_patient():
    print("\n--- Add Patient ---")
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter gender: ")
    disease = input("Enter disease: ")

    data = f"{patient_id},{name},{age},{gender},{disease}\n"

    with open(PATIENT_FILE, 'a') as file:
        file.write(data)

    print("Patient added successfully.")

# =========================
# VIEW PATIENTS
# =========================

def view_patients():
    print("\n--- Patient Records ---")

    with open(PATIENT_FILE, 'r') as file:
        records = file.readlines()

    if not records:
        print("No patient records found.")
        return

    for record in records:
        patient = record.strip().split(',')
        print(f"ID: {patient[0]}")
        print(f"Name: {patient[1]}")
        print(f"Age: {patient[2]}")
        print(f"Gender: {patient[3]}")
        print(f"Disease: {patient[4]}")
        print("----------------------")

# =========================
# ADD DOCTOR
# =========================

def add_doctor():
    print("\n--- Add Doctor ---")
    doctor_id = input("Enter doctor ID: ")
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")

    data = f"{doctor_id},{name},{specialization}\n"

    with open(DOCTOR_FILE, 'a') as file:
        file.write(data)

    print("Doctor added successfully.")

# =========================
# VIEW DOCTORS
# =========================

def view_doctors():
    print("\n--- Doctor Records ---")

    with open(DOCTOR_FILE, 'r') as file:
        records = file.readlines()

    if not records:
        print("No doctor records found.")
        return

    for record in records:
        doctor = record.strip().split(',')
        print(f"ID: {doctor[0]}")
        print(f"Name: {doctor[1]}")
        print(f"Specialization: {doctor[2]}")
        print("----------------------")

# =========================
# BOOK APPOINTMENT
# =========================

def book_appointment():
    print("\n--- Book Appointment ---")
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")

    data = f"{patient_name},{doctor_name},{date},{time}\n"

    with open(APPOINTMENT_FILE, 'a') as file:
        file.write(data)

    print("Appointment booked successfully.")

# =========================
# VIEW APPOINTMENTS
# =========================

def view_appointments():
    print("\n--- Appointment Records ---")

    with open(APPOINTMENT_FILE, 'r') as file:
        records = file.readlines()

    if not records:
        print("No appointment records found.")
        return

    for record in records:
        appointment = record.strip().split(',')
        print(f"Patient: {appointment[0]}")
        print(f"Doctor: {appointment[1]}")
        print(f"Date: {appointment[2]}")
        print(f"Time: {appointment[3]}")
        print("----------------------")

# =========================
# MENU
# =========================

def menu():
    while True:
        print("\n===== CLINIC MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. View Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            add_doctor()
        elif choice == '4':
            view_doctors()
        elif choice == '5':
            book_appointment()
        elif choice == '6':
            view_appointments()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# =========================
# MAIN PROGRAM
# =========================

if __name__ == "__main__":
    create_files()
    menu()
