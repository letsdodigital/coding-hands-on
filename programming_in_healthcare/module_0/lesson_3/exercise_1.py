"""Lesson 3 - exercise 1 - Control the flow

Run the code with:

$ python exercise_1.py

Change the value of 'patient_allergy' to see what happens. 

What is the output?

Gotten stuck, look at the slides at:
https://letsdodigital.org/learn/learn-python/module-0/4-python-basics.html
"""

patient_allergy = "amoxicillin"

if patient_allergy == "amoxicillin":
    allergy_group = "penicillins"
elif patient_allergy == "tazocin":
    allergy_group = "penicillins"
else:
    allergy_group = "other antibiotics"

print("* Patient is allergic to " + allergy_group)

# If that worked, please move on to exercise 2
