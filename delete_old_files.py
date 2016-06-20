# This program deletes the files older than a matching-criterion 

import datetime
import shutil
import os 
from pprint import pprint

# global variables
NOW=45
tree = {}

def run_logs():
    '''
        This function keeps a log of when we ran our program last. This comes handy
        when we might not have run this every day and want to see 'how much' we have to catch up.
        The (CURRENT_TIME - last entry in the file) is how much we need to add to the 'age' in customer
    '''

    last_ran_this_at = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    with open('logfile.txt', "a") as output:
        output.write(last_ran_this_at + "\n")

def dir_to_dict(tree, branches, leaf):
    '''
        The idea behind choosing os.walk is twofold:
            1. we get to take advantage of tree traversal,
            2. hence getting Olog(n) run time complexity
        Build a tree from the given directory structure all the way till leaf nodes
    '''
    
    if len(branches) == 1:
        tree[branches[0]] = leaf
        return
    if not tree.has_key(branches[0]):
        tree[branches[0]] = {}
    dir_to_dict(tree[branches[0]], branches[1:], leaf)

def run_init():
    '''
        Basic inititalization before the helper functions kick off.
    '''

    run_logs()
    startpath = '.'
    for root, dirs, files in os.walk(startpath):
        branches = [startpath]
        if root != startpath:
            branches.extend(os.path.relpath(root, startpath).split('/'))

        dir_to_dict(tree, branches, dict([(d,{}) for d in dirs]+ \
                                  [(f,None) for f in files]))

def set_per_customer_data():
    '''
        This is a matter of choice. We could have gotten this data from an external file of any format.
        In which case we would need to parse into a easily searchable data structure.
        In this example for the sake of simplicity, I constructed a dictionary, which is most efficient
        to search no matter how many customers/device/time nests we have
    '''
    
    customer_metadata = {"c1": 3, "c2": 1, "c3" : 5, "c4" : 10}
    for customer in customer_metadata.keys():
        tree['.'][customer]['age'] = customer_metadata[customer]
    pprint (tree)

def delete_older_than():
    '''
        -The idea behind this function is to slide down to the level of timestamped files we have under
        each device
        -Check if the folder qualifies to be deleted
        -If yes, delete the folder along with everything under it (the 50 files in our example)
        Note: Currently it runs ini worst case O(n^2).
        -But dictionaries/hashtables are very efficient for searches
        in average case, especially this can be extended for distributed systems really well, with
        something like DHT between peers. Of course, that is not part of this current example.
        -to catch up if we miss running some days, ((NOW-int(time))+catch_up_days) > age.
        -catch_up_days can be got from run_logs
    '''

    for customer in tree['.'].keys():
      if type(tree['.'][customer]) == dict:
        age = tree['.'][customer]['age']
        for key, value in tree['.'][customer].iteritems():
          if type(value) == dict:
            device = tree['.'][customer][key]
            for time, value in device.iteritems():
              print NOW, time, age
              if type(value) == dict:
                if (NOW-int(time)) > age:
                  print customer, key, time
                  purge_path = os.path.join(customer,key,time)
                  print "deleting..", purge_path
                  if os.path.exists(purge_path):
                    shutil.rmtree(os.path.join(customer,key,time))

def print_dir():
    print 'tree:'
    pprint(tree)


# process starts here 

run_init()
set_per_customer_data()
delete_older_than()
print_dir()
exit()

# end of process control

