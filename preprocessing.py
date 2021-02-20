import os, sys, shutil



def change_question_name(student_solution_dir, question_names):
    """
    student_solution_dir (str): the path with the solutions of the student
    question_names (list)
    """
    student_name = student_solution_dir.split('\\')[-1] # might not work on macOS
    student_solutions = os.listdir(student_solution_dir)

    unable = student_solutions.copy()
    
    for file in student_solutions:
        for question_name in question_names:
            search_key = f"{'.'.join(question_name[1:].split('_'))}" # [1:] to get rid of 'functions', which is the first key of the testcases dict
            if file.find(search_key) != -1:
                src = os.path.join(student_solution_dir, file)
                dest = os.path.join(student_solution_dir, question_name + '.py')
                os.rename(src, dest)
                unable.remove(file)
                break
            elif file.find(question_name) != -1:
                unable.remove(file)
                break

    return unable


def split_py_files_by_name(lab_number):
    """
    The python files have to have names
    """
    
    parent_dir = os.path.join('./labs', lab_number)

    py_files = list(filter(lambda file: file.endswith('.py') and file != 'testcase.py',os.listdir(parent_dir)))
    
    if len(py_files) == 1:
        logging.warn("There are no files. You need to extract the zip file.")
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

        new_path = os.path.join(parent_dir, name.replace(' ', '_'))
        try:
            os.mkdir(new_path)
            logging.info(f'New directory created at: {new_path}')
        except Exception as e:
            logging.error("There was a problem with creating a new directory to group the student solutions by name.")
            logging.error(e)
        
        for py_file in py_files:
            if py_file.find(name) != -1:
                src = os.path.join(parent_dir, py_file)
                move_loc = shutil.move(src, new_path)
                logging.info(f'{py_file} was moved to {move_loc}')

