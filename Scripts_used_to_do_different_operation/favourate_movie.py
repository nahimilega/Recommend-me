import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["movie_data"]
mycol = mydb["mainpage_movielist"]

top_movie_id=[]

for x in mycol.find():
  if(float(x['imdb'])>8.0):
  	top_movie_id.append(x['id'])

top_movie_id.sort(reverse = True)
print(top_movie_id)  	