import random

test_num = 100

def make_inputs():
    for x in range(test_num):
        myfile = open("inputs/input{0}.in".format(x), 'w')
        date = random.randrange(1, 30)
        month = random.randrange(1, 12)
        year = random.randrange(1000, 3000)
        myfile.write(('0' if date < 10 else '') + str(date) + '/' + ('0' if month<10 else '') + str(month) + '/' + str(year))

make_inputs()

#if __name__ == '__main__':
#    main()
