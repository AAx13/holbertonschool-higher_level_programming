import sys
import peewee
from models import *

my_models_db.connect()

args = ['create', 'print', 'insert', 'delete']

if len(sys.argv) < 2:
    print "Please enter an action"
elif sys.argv[1] not in args:
    print "Undefined action %s" % sys.argv[1]
else:
    print sys.argv[1]
    if sys.argv[1] == 'create':
        my_models_db.create_tables([School, Batch, User, Student])
    if sys.argv[1] == 'print':
