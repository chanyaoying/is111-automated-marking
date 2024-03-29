import os
import sys
import shutil
import json
import datetime
import time
import logging


def mark_question(import_statement, testcases):
    """
    mark one question and output the stats
    """
    start_time = time.time()

    error = []
    score = 0
    percentage = 0

    try:
        exec(import_statement)
    except Exception as e:
        error = "Error detected: Unable to import question function. The function name is probably wrong."
        logging.warn(error)
        logging.warn(e)
        error = [error, str(e)]

        end_time = time.time()
        time_taken = end_time - start_time

        return score, error, percentage, time_taken * 1000

    for i in range(len(testcases)):
        testcase = testcases[i]
        try:
            scoring_code = f"global correct; correct = int({testcase})"
            exec(scoring_code)
            score += correct
        except Exception as e:
            error = [f"Unable to mark test case no.{i+1}", str(e)]

    percentage = score / len(testcases)

    end_time = time.time()
    time_taken = end_time - start_time

    return score, error, percentage, time_taken * 1000


def confirmation(question):

    to_rename = input(question)
    if to_rename.lower() == 'n':
        logging.info(f'User entered \'{to_rename}\'')
        return False
    elif to_rename.lower() == 'y':
        logging.info(f'User entered \'{to_rename}\'')
        return True
    else:
        print("Please enter either 'y' or 'n'.")
        return confirmation(question)


def parse_testcase(parent_dir):

    testcase_dir = os.path.join(parent_dir, 'testcase.txt')
    try:
        with open(testcase_dir, 'r') as file:
            lines = ''.join(file.readlines()).split('\n')

        testcases = {"functions": dict()}

        for line in lines:
            if '#' in line:
                question_number = line[2:]
                question_number = f"q{'_'.join(question_number.split('.'))}"
                testcases[question_number] = []
            elif line:
                question_number = list(testcases.keys())[-1]
                testcases[question_number].append(line[6:-1])
                function = line.split('(')[1]
                if function not in testcases['functions']:
                    testcases['functions'][question_number] = function

    except Exception as e:
        logging.error("Error with the parsing of test case.")
        print("Error with the parsing of test case. Check logs.\nExiting...")
        logging.error(e)
        logging.error(f'Please create a testcase.txt file in {parent_dir}')
        exit()

    return testcases


def parse_date(date_string):
    """
    Converts date_string into datetime objects for comparison.
    """
    m, d, y, t, h12 = (n.replace(',', '').strip()
                       for n in date_string.strip().split(' '))
    hour, minute = t[:-2], t[-2:]
    return datetime.datetime.strptime(f"{d}/{m}/{y} {hour}:{minute} {h12}", "%d/%b/%Y %I:%M %p")

