import os

def scan(path, filt = [], save_to_file = False):
    fileNames = []
    dirName = path
    for (dirName, dirs, files) in os.walk(dirName):

        filtfiles = []
        for filename in files:
            if len(filt) == 0:
                fileNames += [str(os.path.join(dirName, filename))]
    if save_to_file == True:
        myfile = open('list_of_files.txt', 'w')
        for name in fileNames:
            myfile.write(name + '\n')
    return fileNames


def main():
    scan('/home/navid/Codes/github/CodeForces/kbl_didi_ridi/')

if __name__ == "__name__":
    main()
