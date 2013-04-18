import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)
db = connection.students
grades = db.grades.find({'type': 'homework'}).sort([('student_id', 1), ('score', 1)])

student_id = -1
for g in grades:
    if student_id != g['student_id']:
        student_id = g['student_id']
        print g
        db.grades.remove({'student_id': student_id})
