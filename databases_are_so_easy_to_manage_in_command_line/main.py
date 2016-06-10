import sys

actions = ['create', 'print', 'insert', 'delete']

if len(sys.argv) < 2:
    print "Please enter an action"
else:
    for i in range(len(actions)):
        if sys.argv[1] == actions[i]:
            print actions[i]
        elif sys.argv[1] != actions[i]:
            print "Undefined action <%s>" % sys.argv[1]
