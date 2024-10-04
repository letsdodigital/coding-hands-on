"""Lesson 2 - exercise 1 - 'Hello world!' web app style!

Run the app using the command:

$ streamlit run exercise_1.py

Follow the instructions in the comments below.

Gotten stuck, look at the slides at:
https://letsdodigital.org/learn/learn-python/module-1/4-lets-build.html

Warning:
This is not to be used as a real life medical app! This is for training purposes only.
"""

# You need to import the `streamlit` module and set it as an alias of `st`


def main():
    st.title("My first web app")
    st.write("Hello world!")
    return


if __name__ == "__main__":
    main()

# If that worked, please move on to exercise 2
# You also need to stop streamlit using CTRL / CMD - C
# Remember to change the file name in the command line as well, eg
# $ streamlit run exercise_2.py
