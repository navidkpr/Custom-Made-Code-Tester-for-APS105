import os
import string
from path_scanner import scan
from input_maker import make_inputs

compiled_solution_path = "correct_outputs/"
output_path = "user_outputs/"

def delete_files(file_paths): #Tested
    for path in file_paths:
        os.system("rm {0}".format(path));
    are_files_deleted = True
    for path in file_paths:
        if os.path.isfile("./{0}".format(path)):
            are_files_deleted = False
    return are_files_deleted

def compare_strings_ignore_whitespace(s1, s2): #Tested
    remove = string.whitespace
    return s1.translate(None, remove) == s2.translate(None, remove)

def give_compiled(file_name, compiled_file_name): #Tested
    os.system("gcc {0} -lm -o {1}".format(file_name, compiled_file_name)) #If file is unable to compile the program will give user an error
    #if os.path.isFile('./a.out') == False: #Return false if file was unable to compile
    #    return False
    return compiled_file_name

def give_output(input_path, compiled_path): #Tested
    #print("./{} < {} > output.out".format(compiled_path, input_path))
    os.system("./{0} < {1} > output.out".format(compiled_path, input_path))
    outputFile = open("output.out", 'r')
    delete_files(["output.out"])
    return outputFile.read()

def test_input(input_path, solution_compiled_path, compiled_file_path): #Tested
    output1 = give_output(input_path, solution_compiled_path)
    output2 = give_output(input_path, compiled_file_path)
    return compare_strings_ignore_whitespace(output1, output2)

def create_inputs():
    make_inputs();
    return 0

def test_code(lab_number, test_file_name): #Tested
    created_files_paths = ["path_scanner.pyc", "user_compiled_code.out"]
    create_inputs()
    input_files = scan("inputs/")
    #input_files = ["1", "2"]

    compiled_file_path = give_compiled(test_file_name, "user_compiled_code.out")
    if compiled_file_path == False:
        return [false, [-1, -1, -1]]

    solution_compiled_path = "solution.out";
    first_wrong_test = None
    first_wrong_index = None
    correct_output = None
    given_output = None
    x = 1
    for input_path in input_files:
        print(x)
        if test_input(input_path, solution_compiled_path, compiled_file_path) == False and first_wrong_test == None:
            inputFile = open(input_path, 'r');
            first_wrong_test = inputFile.read()
            correct_output = give_output(input_path, solution_compiled_path)
            given_output = give_output(input_path, compiled_file_path)
            first_wrong_index = x
        x = x + 1
    delete_files(input_files + created_files_paths)
    if first_wrong_test != None:
        return [False, [first_wrong_index, first_wrong_test, correct_output, given_output]]
        return [True, []]
#Output for test_code:
# [True, []] -> Correct Code
# [False, [False]] -> Compilation Error
# [False, [input, correct_output, users_output]] -> Wrong Test Case

def main():
    print(test_code(1, "test.c"))


if __name__ == '__main__':
    main();

