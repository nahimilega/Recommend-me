import pandas as pd

#This is used to find the user who have rated the most and the film which was most rated and its intersection as well

df = pd.read_csv("new_links.csv")
a=df.to_numpy()
all_genre={}


movie_id=[]

for x in a:
	movie_id.append(x[0])



df2 = pd.read_csv("movies.csv")

b=df2.to_numpy()


for i in a:
	
		if(i[0] in user_):
			pass
		else:	

			try:
				all_genre[i[0]]=all_genre[i[0]]+1
			except:
				all_genre[i[0]]=1



'''
a=[123]
c=a[20]
'''
sorted_data=dict(sorted(all_genre.items(), key=lambda x: x[1],reverse=True))

print(sorted_data)



'''
sorted_data=dict(sorted(all_data.items(), key=lambda x: x[1],reverse=True))
a=list(sorted_data.keys())
for i in a[:500] :
    print(i, " : ",all_data[str(i)] )


'''




'''
biggest=0

for i in a:
    if(i[0]>biggest):
        biggest=i[0]


print(biggest)        
'''