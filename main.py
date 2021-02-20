import os
from preprocessing import *
from utility import *
from report import report

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

        question_names = list(testcases.keys())

        rename(dirs, parent_dir, question_names)

        result = {}

        for student in dirs:
            student_path = os.path.join(parent_dir, student)

            solution_files = list(filter(lambda file: file.startswith('q') and file.endswith('.py')  ,os.listdir(student_path)))

            student_stats = {}            

            for solution_file in solution_files: # for each question

                if solution_file == "__pycache__":
                    continue

                solution_file_path = os.path.join(student_path, solution_file)
                question = solution_file.rstrip('.py')

                # store information about the question
                stats = {'errors': [], 'prints': 0, 'inputs': 0}

                # count and remove print and input statements
                code = ''
                with open(solution_file_path, 'r') as file:
                    for line in file.readlines():
                        if line.find("print") != -1:
                            stats['prints'] += 1
                        elif line.find("input") != -1:
                            stats['inputs'] += 1
                        else:
                            code += line

                code = ''.join(code)

                # replace code with code without print and input statements
                with open(solution_file_path, "w") as file:
                    file.write(code)

                # load test cases for the question
                question_testcases = testcases[question]

                # import student's function in question
                import_statement = f"from labs.{lab_number}.{student}.{question} import {testcases['functions'][question]}"

                # execute import statement
                try:
                    # unpack into stats
                    score, error, percentage = mark_question(import_statement, question_testcases)
                    stats['score'] = score
                    stats['percentage'] = percentage
                    stats['errors'].extend(error)
                except Exception as e:
                    print("Error: ", e)

                student_stats[question] = stats

            result[student] = student_stats
    
    report(result, parent_dir)