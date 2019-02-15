import pandas as pd

#This is used to find the user who have rated the most and the film which was most rated and its intersection as well

df = pd.read_csv("new_ratings.csv")
a=df.to_numpy()


all_new_user={}
user_id=[]

df2 = pd.read_csv("new_links.csv")
ab=df2.to_numpy()



movie_id=[]

for x in ab:
	movie_id.append(x[0])




f = open("userid.txt", "r")
for x in f:
    user_id.append(float(x[:-2]))


'''
a=[123]
c=a[20]
'''
for i in a:
	if(i[0] in user_id):
		pass
	else:
		try:
			all_new_user[i[0]]=all_new_user[i[0]]+1
		except:
			all_new_user[i[0]]=1 	
    	

sorted_data=dict(sorted(all_new_user.items(), key=lambda x: x[1],reverse=True))
print(sorted_data)



