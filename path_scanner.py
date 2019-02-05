import os

def scan(path, filt = []):
    fileNames = []
    dirName = path
    for (dirName, dirs, files) in os.walk(dirName):

        filtfiles = []
        for filename in files:
            if len(filt) == 0:
                fileNames += [str(os.path.join(dirName, filename))]

    myfile = open('list_of_files.txt', 'w')
    for name in fileNames:
        myfile.write(name + '\n')
    #print(fileNames)
    return fileNames

scan('/home/navid/Codes/github/CodeForces/kbl_didi_ridi/')
