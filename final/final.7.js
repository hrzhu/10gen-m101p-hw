use test

db.albums.ensureIndex({ images: 1 })
db.images.find({ tags: 'kittens' }).count()
