import os
from path_scanner import scan

solution_path = "correct_outputs/"
output_path = "user_outputs/"
inputs_path = "inputs/"

def delete_files(file_paths):
    for path in file_paths:
        os.system("rm {}".format(path));

def is_output_correct(output_path, solution_path):
    text = os.system("diff --strip-trailing-cr {} {}".format(output_path, solution_path))
    print(text)

def test_code(lab_number, file_path):

    os.system("gcc {} -o compiled_solution.out".format(solution_path));

    input_files = scan(inpus_path);
    currentTestNum = 1;

    for path in input_files:

        os.system("./compiled_code.out < {} > user_output".format(path));
        os.system("./{} < {} > solution_output".format(solution_path, path));
        if is_output_correct(user_output, solution_output) == False:
            print("test {}: Wrong".format(currentTestNum));
            return False;
        print("test {}: Correct".format(currentTestNum);
        currentTestNum++;


if __name__ == __main__:
    main();

