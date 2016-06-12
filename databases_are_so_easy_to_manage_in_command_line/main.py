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
    if sys.argv[1] == 'create':
        my_models_db.create_tables([School, Batch, User, Student])
        print "Creating all tables.."

    elif sys.argv[1] == 'print':
        all_models = { 'school': School, 'batch': Batch, 'user': User, 'student': Student }
        if len(sys.argv) < 3:
            print "Format: print <model>"
        else:
            row = all_models[sys.argv[2]].select()
            for i in row:
                print i

    elif sys.argv[1] == 'insert':

        if len(sys.argv) < 3:
            print "Format: insert <model name> [Choices: school, batch, student]" 
        else:

            if sys.argv[2] == 'school':
                if len(sys.argv) < 4:
                    print "Format: school <name>"
                else:
                    insert_new_school = School.create(name=sys.argv[3])
                    print "New %s : %s" % ('School', sys.argv[3])

            if sys.argv[2] == 'batch':
                if len(sys.argv) < 5:
                    print "Format: batch <school id> <name> "
                else:
                    insert_new_batch = Batch.create(school_id=sys.argv[3], name=sys.argv[4])
                    print "New %s : %s" % ('Batch', sys.argv[4])

            if sys.argv[2] == 'student':
                if len(sys.argv) < 7:
                    print "Format: student <batch id> <age> <last_name> <first_name>"
                else:
                    insert_new_student = Student.create(batch_id=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5], first_name=sys.argv[6])
                    print "New %s : %s %s" % ('Student', sys.argv[6], sys.argv[5])

    elif sys.argv[1] == 'delete':
        print sys.argv[1]
