import subprocess

"""Exercise 0 - What the final product will eventually look like

Run this file to see what the final product will look like. This file will run the
script exercise_14.py that you will create in the next exercise.

Play around with the app to see what it does. You can change the values in the
input fields and see how the output changes.

Once you are happy with the final product, you can start working on the exercises.
Press Ctrl+C / Cmd+C to stop the app and continue with the exercise_1.py.
"""

subprocess.run(['streamlit', 'run' , 'exercise_14.py'], check=True, capture_output=True, text=True)