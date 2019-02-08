import random

test_num = 1000

def make_inputs():
    for x in range(test_num):
        myfile = open("inputs/input{0}.in".format(x), 'w')
        myfile.write(str(random.randrange(-12, 12)) + " ")
        myfile.write(str(random.randrange(-12, 12)) + " ")
        myfile.write(str(random.randint(0, 1000)) + "\n")
        myfile.write("0 0 0")

def main():
    make_inputs()

if  __name__ == "__main__":
    main()
