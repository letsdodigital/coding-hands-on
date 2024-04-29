"""Lesson 2

Learning about basic python programming.

Gotten stuck, look at the slides at:
https://letsdodigital.org/learn/learn-python/module-1/

"""

"""Ignore this code up until...

"""

import answers.lesson_2_anwers as answers

all_correct = True


def statement(answer):
    global all_correct
    if not answers.statement(answer):
        all_correct = False
    return


"""... here"""

"""START HERE!"""

"""Exercise 1 - What is in a comment?
What is a comment? Uncomment the correct answer below
"""

# statement("A comment is code that the computer must run.")
# statement("A comment is a pretty addition to the code.")
# statement("A comment is something that every line of code needs.")
# statement("A comment is used to provide helpful information for your later self and others to better understand your code at a later date")
# statement("A comment is a waste of time")

"""Exercise 2 - variables
Uncomment the correct answers
"""

# statement("A variable is a set space in the computer’s memory.")
# statement("A float can store lists of numbers.")
# statement("A dictionary stores key and value pairs.")
# statement("A string can store any character on the keyboard.")
# statement("A boolean can store True, False and maybe.")

"""Exercise 3 - spaces
Uncomment the below code. What happens when you run it from the terminal?
Can you spot the problem and fix it?
"""

# drug name = "Amoxicillin"

"""Exercise 4 - quotation marks
Uncomment the below code. What happens when you run it from the terminal?
Can you spot the problem and fix it?
"""

"""
patient_id = "1523"
patient_name = "John Smith'
patient_DOB = "01/01/1990"
"""

"""Exercise 5 - indentation
Why is the below code not printing out anything? Can you fix it?
"""


def a_function():
    print("* I am a line of code that wants to be printed!")
    return

    a_function()


"""Exercise 6 - naming conventions
Uncomment the correct answers
"""

# statement("snake_case_is_used_for_variables_functions_methods_and_modules.")
# statement("CONSTANT_CASE_IS_USED_FOR_CONSTANTS.")
# statement("CamelCaseIsUsedForClasses.")
# statement("lowercasepackagenamesareusedforpackages.")

"""Exercise 7 - control the flow
Uncomment the below function and try and change the value of 'patient_allergy'
"""

"""
patient_allergy = "amoxicillin"

if patient_allergy == "amoxicillin":
    allergy_group = "penicillins"
elif patient_allergy == "tazocin":
    allergy_group = "penicillins"
else:
    allergy_group = "others"

print("* Patient is allergic to", allergy_group)
"""

""" Exercise 8 - for loops
    Write code to print out each element of the below list
    Hint (use 'for' and 'in')
    Feeling more adventurous, try using 'while' instead
"""

hb_values = [12, 12.3, 12.4, 13]

"""Exercise 9 - calling a function
Convert the comments below into code. A userful link:
https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/calculate-bmi-for-adults
"""


def bmi_calculator(weight, height):
    # write code to calculate BMI ()
    # print out the BMI
    return


# call the bmi_calculator above


# End print
answers.end(all_correct)
