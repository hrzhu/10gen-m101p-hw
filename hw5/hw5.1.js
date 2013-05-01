use blog

db.posts.aggregate([{ $project: {_id: 0, author: '$comments.author'} }, { $unwind: '$author' }, { $group: { _id: '$author', comments: { $sum: 1 } } }, { $sort: { comments: -1 } }, { $limit: 1 }])
