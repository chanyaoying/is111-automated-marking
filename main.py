import os
import logging
from preprocessing import *
from utility import *
from report import report


##############################################
# SETTINGS

lab_number = 4
current_directory = '.'

##############################################


if lab_number < 14:

    lab_number = 'lab' + str(lab_number)
    parent_dir = os.path.join('./labs', lab_number)

    logging_path = os.path.join(parent_dir, 'logs.log')
    logging.basicConfig(level=logging.DEBUG, filename=logging_path,
                        filemode='a', format='%(asctime)s-%(levelname)s-%(message)s')
    logging.info('Process Start.')

    dirs = list(filter(lambda file: file.endswith(
        '_'), os.listdir(parent_dir)))
    if not dirs:
        split_py_files_by_name(parent_dir)
        dirs = list(filter(lambda file: file.endswith(
            '_'), os.listdir(parent_dir)))

    testcases = parse_testcase(parent_dir)

    question_names = list(testcases.keys())[1:]

    rename(dirs, parent_dir, question_names)

    result = {}

    for student in dirs:
        student_path = os.path.join(parent_dir, student)

        solution_files = list(filter(lambda file: file.startswith(
            'q') and file.endswith('.py'), os.listdir(student_path)))

        student_stats = {}
        attempted = question_names.copy()

        for solution_file in solution_files:  # for each question

            logging.info(f"Marking {solution_file} for {student} now.")

            if solution_file == "__pycache__" or solution_file.find('original') != -1:
                continue

            solution_file_path = os.path.join(student_path, solution_file)
            question = solution_file.rstrip('.py')

            # the student attempted this
            if question in attempted:
                attempted.remove(question)

            # store information about the question
            stats = {'errors': [], 'prints': 0, 'inputs': 0}

            # store number of prints and inputs in the question. Original copies are created if there are any.
            stats['prints'], stats['inputs'] = handle_prints_and_inputs(
                student_path, solution_file)

            # load test cases for the question
            question_testcases = testcases[question]

            # import student's function in question (prevents code injection by students)
            import_statement = f"from labs.{lab_number}.{student}.{question} import {testcases['functions'][question]}"

            try:
                # execute import statement and mark questions
                score, error, percentage = mark_question(
                    import_statement, question_testcases)
                stats['score'] = score
                stats['percentage'] = percentage
                stats['errors'].extend(error)
            except Exception as e:
                logging.warn("Error captured: ")
                logging.warn(e)

            student_stats[question] = stats

        for unattempted in attempted:
            student_stats[unattempted] = {
                "errors": ['Question not attempted'],
                "prints": 0,
                "inputs": 0,
                "score": 0,
                "percentage": 0
            }
        result[student.replace('_', ' ').rstrip() + ' _'] = student_stats

report(result, parent_dir)
logging.info('Process ends.')
logging.info(
    '========================================================================')
