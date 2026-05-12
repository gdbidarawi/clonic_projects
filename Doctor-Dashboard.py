import os
from datetime import datetime

PATIENT_FILE = "patients.txt"
APPOINTMENT_FILE = "appointments.txt"
DOCTOR_FILE = "doctors.txt"

# =========================
# HELPERS
# =========================

def load_records(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip().split(',') for line in lines if line.strip()]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# =========================
# DOCTOR DASHBOARD
# =========================

def doctor_dashboard():
    while True:
        clear_screen()
        doctors = load_records(DOCTOR_FILE)
        patients = load_records(PATIENT_FILE)
        appointments = load_records(APPOINTMENT_FILE)

        print("\n" + "=" * 50)
        print("        DOCTOR DASHBOARD")
        print("=" * 50)

        # --- Summary Stats ---
        print(f"\n  Total Doctors      : {len(doctors)}")
        print(f"  Total Patients     : {len(patients)}")
        print(f"  Total Appointments : {len(appointments)}")
        print("\n" + "-" * 50)

        # --- Doctor List ---
        if not doctors:
            print("\n  No doctors registered yet.")
        else:
            print(f"\n  {'ID':<8} {'Name':<20} {'Specialization'}")
            print("  " + "-" * 44)
            for doc in doctors:
                if len(doc) >= 3:
                    print(f"  {doc[0]:<8} {doc[1]:<20} {doc[2]}")

        print("\n" + "=" * 50)
        print("  DASHBOARD MENU")
        print("=" * 50)
        print("  1. View my appointments")
        print("  2. View all patients")
        print("  3. Search patient by name")
        print("  4. View today's appointments")
        print("  5. Add new doctor")
        print("  6. Back to main menu")
        print("=" * 50)

        choice = input("\n  Enter choice: ").strip()

        if choice == '1':
            view_doctor_appointments(doctors, appointments)
        elif choice == '2':
            view_all_patients_dashboard(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            view_today_appointments(appointments)
        elif choice == '5':
            add_doctor()
        elif choice == '6':
            break
        else:
            input("\n  Invalid choice. Press Enter to continue...")

def view_doctor_appointments(doctors, appointments):
    clear_screen()
    print("\n" + "=" * 50)
    print("  SELECT DOCTOR")
    print("=" * 50)

    if not doctors:
        print("  No doctors found.")
        input("\n  Press Enter to go back...")
        return

    for i, doc in enumerate(doctors, 1):
        print(f"  {i}. {doc[1]} ({doc[2]})")

    print("  0. Back")
    choice = input("\n  Enter number: ").strip()

    if choice == '0' or not choice.isdigit():
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(doctors):
        return

    selected_doctor = doctors[idx][1]

    clear_screen()
    print("\n" + "=" * 50)
    print(f"  APPOINTMENTS FOR: {selected_doctor.upper()}")
    print("=" * 50)

    found = False
    for appt in appointments:
        if len(appt) >= 4 and appt[1].lower() == selected_doctor.lower():
            print(f"\n  Patient : {appt[0]}")
            print(f"  Date    : {appt[2]}")
            print(f"  Time    : {appt[3]}")
            print("  " + "-" * 30)
            found = True

    if not found:
        print(f"\n  No appointments found for {selected_doctor}.")

    input("\n  Press Enter to go back...")

def view_all_patients_dashboard(patients):
    clear_screen()
    print("\n" + "=" * 50)
    print("  ALL PATIENTS")
    print("=" * 50)

    if not patients:
        print("\n  No patients registered.")
    else:
        print(f"\n  {'ID':<8} {'Name':<18} {'Age':<6} {'Gender':<8} {'Disease'}")
        print("  " + "-" * 52)
        for p in patients:
            if len(p) >= 5:
                print(f"  {p[0]:<8} {p[1]:<18} {p[2]:<6} {p[3]:<8} {p[4]}")

    input("\n  Press Enter to go back...")

def search_patient(patients):
    clear_screen()
    print("\n" + "=" * 50)
    print("  SEARCH PATIENT")
    print("=" * 50)

    keyword = input("\n  Enter patient name to search: ").strip().lower()
    results = [p for p in patients if len(p) >= 2 and keyword in p[1].lower()]

    print()
    if not results:
        print("  No matching patients found.")
    else:
        for p in results:
            print(f"\n  ID      : {p[0]}")
            print(f"  Name    : {p[1]}")
            print(f"  Age     : {p[2]}")
            print(f"  Gender  : {p[3]}")
            print(f"  Disease : {p[4]}")
            print("  " + "-" * 30)

    input("\n  Press Enter to go back...")

def view_today_appointments(appointments):
    clear_screen()
    today = datetime.now().strftime("%Y-%m-%d")
    print("\n" + "=" * 50)
    print(f"  TODAY'S APPOINTMENTS ({today})")
    print("=" * 50)

    found = False
    for appt in appointments:
        if len(appt) >= 4 and appt[2] == today:
            print(f"\n  Patient : {appt[0]}")
            print(f"  Doctor  : {appt[1]}")
            print(f"  Time    : {appt[3]}")
            print("  " + "-" * 30)
            found = True

    if not found:
        print(f"\n  No appointments scheduled for today ({today}).")
        print("  Tip: Book appointments using date format YYYY-MM-DD")

    input("\n  Press Enter to go back...")

def add_doctor():
    clear_screen()
    print("\n" + "=" * 50)
    print("  ADD NEW DOCTOR")
    print("=" * 50)

    doctor_id = input("\n  Enter doctor ID: ")
    name = input("  Enter doctor name: ")
    specialization = input("  Enter specialization: ")

    data = f"{doctor_id},{name},{specialization}\n"
    with open(DOCTOR_FILE, 'a') as file:
        file.write(data)

    print("\n  Doctor added successfully!")
    input("\n  Press Enter to go back...")
