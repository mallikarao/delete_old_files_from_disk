Environment:
Python 2.7.9 (default, Apr  7 2015, 07:58:25) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin

Time programming started: 4:20 PM, June 19, 2016
Time programming ended: 6:00 PM, June 19, 2016

How to run.

-go to any directory
Copy and chdir to the folder 06_19_project
#python create_dir.py
--this creates the necessary directory structure similar to the one described in the question, which serves as a test dir

#delete_old_files.py

#cleanup.py
--removes the test_dir created by create_dir.py


Purpose of each file:

1. create_dir.py:
Creates the directory structure required to test the project
Here is a snapshot of how the test directory looks like.
This is ready now to be run against delete_old_files.py

[mallikarao@Shire test_dir (mallika_myapp)]$ lsdir
   |-c1
   |---d1
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d2
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d3
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d4
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |-c2
   |---d1
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d2
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d3
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d4
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |-c3
   |---d1
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d2
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d3
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d4
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |-c4
   |---d1
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d2
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d3
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
   |---d4
   |-----40
   |-----41
   |-----42
   |-----43
   |-----44
   |-----45
   |-----46
   |-----47
   |-----48
   |-----49
[mallikarao@Shire test_dir (mallika_myapp)]$ 

2. delete_old_files.py:
 -Converts the directory structure to a dictionary
 -uses tree traversal to parse through all files under test_dir(os.walk)
 -tests for condition, based on age per customer. Age is metadata in customer file level.
 -Also tells us what all files were deleted.
 -logs when we ran the delete_old_files.py for the last time into a log file. This helps us to calculate how long ago we ran it and how much more should we delete.

3. cleanup.py:
 -remove the so created test_dir, this was only for demo purposes.


