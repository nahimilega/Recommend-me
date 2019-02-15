import pandas as pd
import numpy as np
import csv


movie_id=[]
f = open("movie_id.txt", "r")
for x in f:
    one_line=x[:-2]
    movie=float(one_line[:one_line.find(':')])
    movie_id.append(movie)

print(len(movie_id))
if( 8784 in movie_id):
    print("prob")
movie_id.sort()
#print(movie_id)
user_id=[]
f = open("userid.txt", "r")
for x in f:
    user_id.append(float(x[:-2]))

with open('sorted_movie_id.txt', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(str(movie_id))


writeFile.close()

df = pd.read_csv("new_ratings.csv")
a=df.to_numpy()
previous_user_id=1
current_user_id=1

one_user_row=list(np.zeros(499))
final_matrix=[]
#Exploiting upon the fact that rating are arrange according the user increasing order
for i in a:
	current_user_id=i[0]
	if (current_user_id in user_id ):
		index=movie_id.index(int(i[1]))
		one_user_row[index]=i[2]
		if(previous_user_id!=current_user_id):
			final_matrix.append(list(one_user_row))
			one_user_row=np.zeros(499)

		previous_user_id=current_user_id		



with open('user_rating_matrix.txt', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(final_matrix)