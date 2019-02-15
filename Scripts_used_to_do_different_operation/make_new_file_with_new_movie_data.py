import csv
import pandas as pd

movie_id=[]
f = open("movie_id.txt", "r")
for x in f:
    one_line=x[:-2]
    movie=float(one_line[:one_line.find(':')])
    movie_id.append(movie)

'''
a=[123]
c=a[20]
'''


df = pd.read_csv("ratings.csv")

a=df.to_numpy()
useful=[]

for i in a:
    if i[1] in movie_id :
    
        useful.append(list(i))


with open('new_ratings.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(useful)








writeFile.close()
