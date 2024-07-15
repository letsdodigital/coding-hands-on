"""Lesson 1 - exercise 2 - Use that class

    We have created a class for you called Patient.

    Follow the instructions in the comments below.

    Run the below code in the terminal using the below command:

    $ python exercise_2.py

    Did you get the results you expected?

    Gotten stuck, look at the slides at:
    https://letsdodigital.org/learn/learn-python/module-0/3-python-basics.html
    https://letsdodigital.org/learn/learn-python/module-1/3-python.html
"""


class Patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.is_admitted = False

    def admit(self):
        if not self.is_admitted:
            print(
                f"Admitting {self.name} to the hospital with diagnosis: {self.diagnosis}"
            )
            self.is_admitted = True
        else:
            print(f"{self.name} is already admitted")

    def discharge(self):
        if self.is_admitted:
            print(f"Discharging {self.name} from the hospital")
            self.is_admitted = False
        else:
            print(f"{self.name} is not currently admitted")


# Create an instance of the Patient class, call this `patient_1`
# Give this patient a name, age and diagnosis

# Create an instance of the Patient class, call this `patient_2`
# Give this patient a name, age and diagnosis

# Admit patient_1
# Admit patient_2

# Discharge patient_1
# Discharge patient_2

# If that all worked, let your tutor know that you have finished.
