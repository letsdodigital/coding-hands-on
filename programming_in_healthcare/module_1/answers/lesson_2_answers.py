""" Lesson 1 answers"""


def statement(question, answer) -> bool:
    """Checks if question and answer match"""
    global all_correct

    question_and_answers: dict[str, str] = {
        "A comment is code that the computer must run.": False,
        "A comment is a pretty addition to the code.": False,
        "A comment is something that every line of code needs.": False,
        "A comment is used to provide helpful information for your later self and others to better understand your code at a later date": True,
        "A comment is a waste of time": False,
        "A variable is a set space in the computer's memory.": True,
        "A float can store lists of numbers.": False,
        "A dictionary stores key and value pairs.": True,
        "A string can store any character on the keyboard.": True,
        "A boolean can store True, False and maybe.": False,
        "snake_case_is_used_for_variables_functions_methods_and_modules.": True,
        "CONSTANT_CASE_IS_USED_FOR_CONSTANTS.": True,
        "CamelCaseIsUsedForClasses.": True,
        "lowercasepackagenamesareusedforpackages.": True,
    }

    if answer == "not answered":
        return True

    if answer != True and answer != False:
        raise ValueError(
            "Answer must be 'True', 'False' or 'not answered'. Please correct this and try again."
        )

    if question not in question_and_answers:
        raise ValueError(
            f"Question '{ question }' is not in the dictionary. Please provide a valid question."
        )

    if (
        question in question_and_answers
        and question_and_answers[question] == answer
    ):
        print(f"* Correct, '{answer}' is the correct answer for '{question}'!")
        return True
    else:
        print(
            f"* Sorry, '{answer}' is not the correct answer for '{question}'."
        )
        return False


def end(all_correct):
    if all_correct:
        print("* All passed!", "\U0001f600")
    else:
        print(
            "* Sorry, there was an some errors / incorrect answers!",
            "\U0001F641",
        )
