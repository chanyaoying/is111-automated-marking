import os
import sys
import shutil
import json
import logging
from utility import confirmation


def handle_prints_and_inputs(student_path, solution_file):
    """
    Creates a copy of the code without input() and print() functions, and marks that copy. Will save the original copy with a '-original' tag.
    Returns the number of prints and inputs respectively.
    """
    # initialise
    prints, inputs, code = 0, 0, ''

    solution_file_path = os.path.join(student_path, solution_file)

    # opens the original and checks for prints and inputs
    with open(solution_file_path, 'r') as file:
        for line in file.readlines():
            if line.find("print") != -1:
                prints += 1
                code += (line[:line.find('print')] + 'pass\n') # replace that line with print() with pass
            elif line.find("input") != -1:
                inputs += 1
                code += 'pass\n' # replace that line with input() with pass
            else:
                code += line

    if prints or inputs:

        originals_path = os.path.join(student_path, 'original_solutions')
        
        try:
            # create 'original_solutions' folder
            os.mkdir(originals_path)
            logging.info("Created a folder with the original solution")
        except OSError as e:
            logging.warn(e)
        except Exception as e:
            logging.error(e)
        finally:
            # original solution path
            new_path = os.path.join(originals_path, solution_file)
            
            # move original solutions into 'original_solutions'
            shutil.move(solution_file_path, new_path)
            logging.info(f"Moved original {solution_file} from {solution_file_path} to {new_path}")

            # create copies that have no print() or input()
            with open(solution_file_path, 'w') as file:
                file.write(code)
            logging.info(f'Created copies without print() and input() in {new_path}')

    return prints, inputs


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


def change_question_name(student_solution_dir, question_names):
    """
    student_solution_dir (str): the path with the solutions of the student
    question_names (list)
    """

    student_solutions = os.listdir(student_solution_dir)

    unable = student_solutions.copy()

    for file in student_solutions:
        for question_name in question_names:
            search_key = f"{'.'.join(question_name.split('_'))[1:]}"
            if file.find(search_key) != -1:
                src = os.path.join(student_solution_dir, file)
                dest = os.path.join(student_solution_dir,
                                    question_name + '.py')
                os.rename(src, dest)
                unable.remove(file)
                break
            elif file.find(question_name) != -1:
                unable.remove(file)
                break

    return unable


def split_py_files_by_name(path):
    """
    The python files have to have names
    """

    py_files = list(filter(lambda file: file.endswith('.py')
                           and file != 'testcase.py', os.listdir(path)))

    if len(py_files) <= 1:
        logging.warn("There are no files. You need to extract the zip file.")
        logging.info("Exiting...")
        print("Exiting...")
        exit()

    dirs_info = [file.split('-') for file in py_files]
    # print(dirs_info)
    # dirs_info.remove(dirs_info.index(['testcase.py']))

    names = []
    for file in dirs_info:
        names.append(file[2].strip())

    names = list(set(names))

    for name in names:

        new_path = os.path.join(path, name.replace(' ', '_'))
        try:
            os.mkdir(new_path)
            logging.info(f'New directory created at: {new_path}')
        except Exception as e:
            logging.error(
                "There was a problem with creating a new directory to group the student solutions by name.")
            logging.error(e)

        for py_file in py_files:
            if py_file.find(name) != -1:
                src = os.path.join(path, py_file)
                move_loc = shutil.move(src, new_path)
                logging.info(f'{py_file} was moved to {move_loc}')
