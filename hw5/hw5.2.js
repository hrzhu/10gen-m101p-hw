use test

db.zips.aggregate([{ $match: { $or: [{ state: 'NY' }, { state: 'CA' }] } }, { $group: { _id: { city: '$city', state: '$state' }, pop: { $sum: '$pop'} } }, { $match: { pop: { $gt: 25000 } } }, { $group: {  _id: null, avg: { $avg: '$pop' } } }])
