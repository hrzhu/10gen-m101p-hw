import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.school
students = db.students

cursor = students.find({}, {'scores': 1})

for entry in cursor:
    _id = entry['_id']
    scores = entry['scores']

    hw_scores = []

    for score in scores:
        if score['type'] == 'homework':
            hw_scores.append(score['score'])

    hw_scores.sort()

    scores.remove({'type': 'homework', 'score': hw_scores[0]})

    students.update({'_id': _id}, {'$set': {'scores': scores}})
