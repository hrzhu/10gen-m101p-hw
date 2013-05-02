use test

db.zips.aggregate([{ $match: { city: { $regex: /^[0-9]/ } } }, { $group: { _id: null, sum: { $sum: '$pop' } } }])
