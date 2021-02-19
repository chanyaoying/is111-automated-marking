
import os
import sys
import shutil
import json
from preprocessing import split_py_files_by_name, change_question_name
from utility import mark_question, parse_testcase, confirmation

# lab_number = input('Which lab assignment are you marking? ')

##############################################
# SETTINGS

lab_number = 4
current_directory = '.'


##############################################

if __name__ == "__main__":

    if lab_number < 14:

        lab_number = 'lab' + str(lab_number)
        parent_dir = os.path.join('./labs', lab_number)

        dirs = list(filter(lambda file: file.endswith(
            '_'), os.listdir(parent_dir)))
        if not dirs:
            split_py_files_by_name(lab_number)
            dirs = list(filter(lambda file: file.endswith(
                '_'), os.listdir(parent_dir)))

        # extract test case
        testcases = parse_testcase(parent_dir)
        question_names = list(testcases.keys())

        need_rename = {}

        for student in dirs:
            student_path = os.path.join(parent_dir, student)
            # change question name
            unable = change_question_name(student_path, question_names)
            if unable:
                need_rename[student] = unable

        if need_rename:
            print("These files need to be renames to their question number: ")
            print(json.dumps(need_rename, indent=4))
            answer = confirmation(
                'Continue marking without renaming the above files? (y/n): ')
            if not answer:
                print("Exiting...")
                exit()

        for student in dirs:
            student_path = os.path.join(parent_dir, student)

            solution_files = os.listdir(student_path)

            for solution_file in solution_files:

                # per question
                solution_file_path = os.path.join(student_path, solution_file)

                # count and remove print statements
                with open(solution_file_path, 'r') as file:
                    code = [line for line in file.readlines()
                            if line.find("print") == -1]
                code = ''.join(code)
                exec(code)
