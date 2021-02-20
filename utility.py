import os, sys, shutil, json, logging
from preprocessing import *


def rename(dirs, parent_dir, question_names):
    need_rename = {}

    for student in dirs:
        student_path = os.path.join(parent_dir, student)
        # change question name
        unable = change_question_name(student_path, question_names)
        if unable:
            need_rename[student] = unable

    if need_rename:
        logging.info(json.dumps(need_rename, indent=4))
        logging.info("Displayed files to be renamed.")
        
        print("These files need to be renames to their question number: ")
        print(json.dumps(need_rename, indent=4))

        answer = confirmation(
            'Continue marking without renaming the above files? (y/n): ')
        if not answer:
            logging.info('User cancelled the process. Exiting...')
            print("Exiting...")
            exit()


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
        confirmation(question)


def parse_testcase(parent_dir):

    testcase_dir = os.path.join(parent_dir, 'testcase.py')
    try:
        with open(testcase_dir, 'r') as file:
            lines = ''.join(file.readlines()).split('\n')
    except Exception as e:
        logging.error("Error with the parsing of test case.")
        logging.error(e)
        logging.error(f'Please create a testcase.py file in {parent_dir}')
    
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

    return testcases


def mark_question(import_statement, testcases):
    """
    mark one question and output the stats
    if error, note it as an error instead of 0
    """
    error = []
    score = 0
    percentage = 0

    try:
        exec(import_statement)
    except Exception as e:
        error = "Error detected: Unable to import question function. The function name is probably wrong."
        logging.warn(error)
        logging.warn(e)
        error =[error, str(e)]
        return score, error, percentage

    for i in range(len(testcases)):
        testcase = testcases[i]
        try: 
            scoring_code = f"global correct; correct = int({testcase})"
            exec(scoring_code)
            score += correct
        except Exception as e:
            error = [f"Unable to mark test case no.{i+1}"]

    percentage = score / len(testcases)

    return score, error, percentage
    