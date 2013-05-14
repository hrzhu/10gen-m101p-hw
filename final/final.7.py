import pymongo

con = pymongo.MongoClient("mongodb://localhost")

db = con.test
images = db.images
albums = db.albums

cursor = images.find({}, {'_id': 1})

for c in cursor:
    image_id = c['_id']
    image_in_albums = albums.find_one({'images': image_id})

    if not image_in_albums:
        images.remove({'_id': image_id})

print 'compeleted'
