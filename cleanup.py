# This program removes and cleans up the test directory created to test this project

import shutil

mydir="./test_dir/"
try:
    shutil.rmtree(mydir)
except OSError, e:
    print ("Error: %s - %s." % (e.filename,e.strerror))

