import os
import sys
import shutil
import json
import logging
from utility import confirmation, parse_date


def parse(student_path, solution_file):
    """
    Creates a copy of the code without input(), print(), exit(), and quit() functions, and marks that copy. Will save the original copy in 'original_solutions'.
    Returns the number of prints, inputs, and lines respectively.
    """
    # initialise
    prints, inputs, no_of_lines, code = 0, 0, 0, ''

    solution_file_path = os.path.join(student_path, solution_file)

    # opens the original and checks for prints and inputs
    with open(solution_file_path, 'r', errors='ignore') as file:
        for line in file.readlines():
            if "print(" in line or "print (" in line:
                prints += 1
                # replace that line with print() with pass
                code += 'pass\n'
            elif "input(" in line or "input (" in line:
                inputs += 1
                code += 'pass\n'  # replace that line with input() with pass
            elif "quit(" in line:
                code += 'pass\n'
            elif "exit(" in line:
                code += 'pass\n'
            else:
                no_of_lines += 1
                code += line

    if prints or inputs:

        originals_path = os.path.join(student_path, 'original_solutions')

        try:
            # create 'original_solutions' folder
            os.mkdir(originals_path)
            logging.info("Created a folder with the original solution")
        except OSError as e:
            logging.info(e)
        except Exception as e:
            logging.error(e)
        finally:
            # original solution path
            new_path = os.path.join(originals_path, solution_file)

            # move original solutions into 'original_solutions'
            shutil.move(solution_file_path, new_path)
            logging.info(
                f"Moved original {solution_file} from {solution_file_path} to {new_path}")

            # create copies that have no print() or input()
            with open(solution_file_path, 'w') as file:
                file.write(code)
            logging.info(
                f'Created copies without nasty functions in {new_path}')

    return prints, inputs, no_of_lines


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

        print("These files need to be renamed to their question number: ")
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

    # to_rename has the following structure:
    # to_rename = {'q2.1': [
    #                       {'src': <some path>, 'dest': <some path>, date: <parsed date>},  <-- earlier version
    #                       {'src': <some path>, 'dest': <some path>, date: <parsed date>}
    #                      ]
    #              'q2.2': [{'src': <some path>, 'dest': <some path>, date: <parsed date>}],
    #              'q3.1': ...
    #               }
    to_rename = {}

    for file in student_solutions:
        for question_name in question_names:

            # we are looking for the keyword: 2.1
            search_key = f"{'.'.join(question_name.split('_'))[1:]}"

            if file.find(search_key) != -1:

                src = os.path.join(student_solution_dir, file)
                dest = os.path.join(student_solution_dir,
                                    question_name + '.py')
                date = parse_date(file.split('-')[3])

                payload = {'src': src, 'dest': dest, 'date': date}
                to_rename.setdefault(question_name, []).append(payload)

                # os.rename(src, dest)
                unable.remove(file)
                break
            elif file.find(question_name) != -1:
                # cases where the file has already been renamed to q2.1.py
                unable.remove(file)
                break

    # rename them, and if earlier versions are found, store them in 'earlier_version'
    for question, metadata in to_rename.items():
        # error handling
        if not len(metadata):
            print("An error occurred. Please check the logs.\nExiting...")
            logging.error(
                f"There are no metadata for {question}.\nmetadata: {metadata}.")
            exit()
        elif len(metadata) > 1:
            logging.info(f'Found earlier versions of {question}.')

            # get the latest one
            metadata = sorted(metadata, key=lambda n: n['date'])
            latest = metadata.pop()

            # the earlier ones will be moved to 'earlier_versions'
            ev_path = os.path.join(student_solution_dir, 'earlier_versions')

            # create ev_path if not exists
            if 'earlier_versions' not in os.listdir(student_solution_dir):
                os.mkdir(ev_path)

            for data in metadata:
                shutil.move(data['src'], ev_path)
                logging.info(f"Moved {data['src']} to 'earlier_versions'")
        else:
            latest = metadata[0]

        # latest one will be renamed
        os.rename(latest['src'], latest['dest'])
        logging.info('Latest versions have been renamed.')

    return unable


def split_py_files_by_name(path):
    """
    Takes all the freshly extracted .py solutions and group them into folders by name.
    """

    py_files = list(filter(lambda file: file.endswith('.py')
                           and file != 'testcase.py', os.listdir(path)))

    if len(py_files) <= 1:
        logging.warn("There are no files. You need to extract the zip file.")
        logging.info("Exiting...")
        print("Exiting...")
        exit()

    dirs_info = [file.split('-') for file in py_files]

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
