import os, sys, shutil, json
from preprocessing import *
from utility import *

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

        testcases = parse_testcase(parent_dir)
        # print(json.dumps(testcases, indent=4))
        # exit()

        question_names = list(testcases.keys())

        rename(dirs, parent_dir, question_names)

        for student in dirs:
            student_path = os.path.join(parent_dir, student)

            solution_files = os.listdir(student_path)

            for solution_file in solution_files:
                solution_file_path = os.path.join(student_path, solution_file)

                # count and remove print statements
                prints = 0
                code = ''
                with open(solution_file_path, 'r') as file:
                    for line in file.readlines():
                        if line.find("print") != -1:
                            prints += 1
                        else:
                            code += line

                code = ''.join(code)

                print(solution_file)
                print(prints)
                exit()
