
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#myclient = pymongo.MongoClient("mongodb://admin:pass1234@cluster0-shard-00-00-qhthx.mongodb.net:27017,cluster0-shard-00-01-qhthx.mongodb.net:27017,cluster0-shard-00-02-qhthx.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb=myclient['movie_data'] 
maintable = mydb["mainpage_movielist"]



data = maintable.find({'id': 20},{'id':30})
print(data)
print(type(data))