import os
import shutil

def build_test_dir():
    shutil.rmtree('test_dir', ignore_errors=True)
    os.mkdir('test_dir')
    os.chdir('test_dir')

    for i in range(1,5):
        fileName = 'c%d' % i
        print fileName
        os.mkdir(fileName)
        os.chdir(fileName)
        for j in range(1,5):
            fileName = 'd%d' % j
            print fileName
            os.mkdir(fileName)
            os.chdir(fileName)
            for x in range(40,50):
              filename = '%d' % x
              print filename
              os.mkdir(filename)
              os.chdir(filename)
              for k in range(0,2):
                try:
                    with open('file%d_%d_%d.txt' % (i,j,k), 'w'):
                        pass
                except IOError:
                    pass
              os.chdir('..')
            os.chdir('..')
        os.chdir('..')
        
build_test_dir()
