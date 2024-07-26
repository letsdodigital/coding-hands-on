patient_name = ""


def patient_info():
    global patient_name
    patient_name = "Alice Smith"
    print(f"Patient Name: {patient_name}")


patient_info()
print(patient_name)
