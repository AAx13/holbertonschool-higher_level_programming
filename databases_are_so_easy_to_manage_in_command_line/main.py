import sys

''' This script will check arguments passed and if it matches our arguments return it, otherwise return an error '''
args = ['create', 'print', 'insert', 'delete']

if len(sys.argv) < 2:
    print "Please enter an action"
elif sys.argv[1] not in args:
    print "Undefined action %s" % sys.argv[1]
else:
    print sys.argv[1]
