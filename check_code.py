import os
import string
from path_scanner import scan

compiled_solution_path = "correct_outputs/"
output_path = "user_outputs/"
inputs_path = "inputs/"

def delete_files(file_paths): #Tested
    for path in file_paths:
        os.system("rm {}".format(path));

def compare_strings_ignore_whitespace(s1, s2): #Tested
    remove = string.whitespace
    return s1.translate(None, remove) == s2.translate(None, remove)

def give_compiled(file_name, compiled_file_name): #Tested
    os.system("gcc {} -o {}".format(file_name, compiled_file_name))
    return compiled_file_name

def give_output(input_path, compiled_path): #Tested
    #print("./{} < {} > output.out".format(compiled_path, input_path))
    os.system("./{} < {} > output.out".format(compiled_path, input_path))
    outputFile = open("output.out", 'r')
    delete_files(["output.out"])
    return outputFile.read()

def test_input(input_path, solution_compiled_path, compiled_file_path): #Tested
    output1 = give_output(input_path, solution_compiled_path)
    output2 = give_output(input_path, compiled_file_path)
    return compare_strings_ignore_whitespace(output1, output2)

def make_inputs(lab_number):
    return 0

def test_code(lab_number, test_file_name): #Tested
    created_files_paths = ["path_scanner.pyc", "user_compiled_code.out"]
    #make_inputs(lab_number, input_path)
    #input_files = scan(input_path)
    input_files = ["1", "2"]

    compiled_file_path = give_compiled(test_file_name, "user_compiled_code.out")

    solution_compiled_path = "solution.out";
    first_wrong_test = None
    correct_output = None
    given_output = None

    for input_path in input_files:
        if test_input(input_path, solution_compiled_path, compiled_file_path) == False:
            inputFile = open(input_path, 'r');
            first_wrong_test = inputFile.read()
            correct_output = give_output(input_path, solution_compiled_path)
            given_output = give_output(input_path, compiled_file_path)
    delete_files(input_files + created_files_paths)
    if first_wrong_test != None:
        return [False, [first_wrong_test, correct_output, given_output]]
    return [True, []]

def main():
    print(test_code(1, "test.c"))


if __name__ == '__main__':
    main();

