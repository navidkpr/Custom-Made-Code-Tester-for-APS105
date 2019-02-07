import unittest
import code_tester
import os

class Test_code_tester(unittest.TestCase):
    def test_delete_files(self):
        open("test_file.tst", "w")
        was_file_deleted = code_tester.delete_files(["test_File.tst"])
        print(was_file_deleted)
        if was_file_deleted == False:
            os.system("rm test_file.tst")
        return was_file_deleted

    def test_compare_strings(self):
        self.assertEqual(code_tester.compare_strings_ignore_whitespace("", "hi"), False)
        self.assertEqual(code_tester.compare_strings_ignore_whitespace("hi\n", "hi"), True)
        self.assertEqual(code_tester.compare_strings_ignore_whitespace("hi", "hi"), True)
        self.assertEqual(code_tester.compare_strings_ignore_whitespace("", ""), True)
        self.assertEqual(code_tester.compare_strings_ignore_whitespace("hello \n this is me 231142 \n \n \n"," hello \n this is me 231142 \n \n"), True)

    def test_give_output(self):
        input_file = 'test_files/sample_input.tst'
        output_file = open('test_files/sample_output.tst', 'r')
        sample_output = output_file.read()

        sample_compiled = 'test_files/sample_compiled.tst'
        self.assertEqual(code_tester.give_output(input_file, sample_compiled), sample_output)
        self.assertEqual(code_tester.give_output(input_file,input_file), False)

    #def test_test_input(self):


    #def test_give_compiled(self):

    #def test_make_inputs(self):

    #def test_test_code(self):


if __name__ == "__main__":
    unittest.main()
