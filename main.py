import pandas as pd
import os
import threading
import time
import pyautogui


def mark_question(q, script, test_cases, max_marks=False):
    """
    ----
    q:
    <class 'str'>
    The question number.
    ----
    script:
    <class 'str'>
    The script to mark against. Indentation and everything must be there.
    ----
    test_cases:
    <class 'list'>
    A list of test cases, which are strings.
    ----
    max_marks: (not implemented yet)
    <class 'bool'>
    Defaults to false. If true, the maximum marks corresponds to the number of test cases. If false, the marks can only be 1 or 0.
    ----
    """
    try:
        marks = 0

        for i in range(len(test_cases)):

            test_case = test_cases[i]

            try:
                exec(script)
                print(f"Passed test case no.{i + 1}")
                marks += 1
            except:
                print(f"Failed test case no.{i + 1}")

    except:
        print(f"Failed to mark {q}.")
        # push 0 marks
    finally:
        print(f"Marked {q}. Marks: {marks}")

code = """
x = "hello world"
print(x)
"""
mark_question('q1.1-test', code, ['yay', 'nay'])


# 0. set up with lab to mark
# lab_number = int(input("Which lab will you be marking?"))

# 0.5 load test case and test_scripts

# 1. for loop to mark through the students' labs


# 2. check against test case
# path = f"./labs/lab{lab_number}/test_case.py"

# 3. allocate marks

# 4. export into csv (with same basic analysis? Highlight students who scored 0, give comments)