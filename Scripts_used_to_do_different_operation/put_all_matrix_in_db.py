import pymongo
import numpy as np
import json
myclient = pymongo.MongoClient("mongodb://admin:pass1234@cluster0-shard-00-00-qhthx.mongodb.net:27017,cluster0-shard-00-01-qhthx.mongodb.net:27017,cluster0-shard-00-02-qhthx.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb=myclient['movie_data'] 
maintable = mydb["mainpage_all_computed_matrix"]

f = open("movie_movie.txt", "r")
final_matrix=[]
for x in f:
    if(x!='\n'):
        new=list(map(float,x.split(',')))
        
        final_matrix.append(new)


arrr=np.array(final_matrix) 
b = arrr.tolist() 
aaa=json.dumps(b)

mydict={"movie_movie": aaa}

maintable.insert_one(mydict)