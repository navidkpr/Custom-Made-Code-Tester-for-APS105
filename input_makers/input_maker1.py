import random

test_num = 300;

def make_inputs():
    for x in range(test_num):
        myfile = open("inputs/input{0}.in".format(x), 'w');
        myfile.write(str(random.randrange(0, 100000000)));

def main():
    make_inputs()

if __name__== "__main__":
    main()
