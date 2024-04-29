""" Lesson 1 answers"""


def statement(answer) -> bool:
    """Checks if question and answer match"""
    global all_correct

    answer_bank: list[str] = [
        "A comment is used to provide helpful information for your later self and others to better understand your code at a later date",
        "A variable is a set space in the computer’s memory.",
        "A dictionary stores key and value pairs.",
        "A string can store any character on the keyboard.",
        "snake_case_is_used_for_variables_functions_methods_and_modules.",
        "CONSTANT_CASE_IS_USED_FOR_CONSTANTS.",
        "CamelCaseIsUsedForClasses.",
        "lowercasepackagenamesareusedforpackages.",
    ]

    if answer in answer_bank:
        print(f"* Correct, '{ answer }'!")
        return True

    else:
        print(f"* Sorry, the following statement is not correct: '{ answer }'")
        return False

    return


def end(all_correct):
    if all_correct:
        print("* All passed!", "\U0001f600")
    else:
        print(
            "* Sorry, there was an some errors / incorrect answers!",
            "\U0001F641",
        )
