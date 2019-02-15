import pandas as pd

#This is used to find the user who have rated the most and the film which was most rated and its intersection as well

df = pd.read_csv("new_ratings.csv")

a=df.to_numpy()
all_data={}
user_id=[]
f = open("userid.txt", "r")
for x in f:
    user_id.append(float(x[:-2]))


'''
a=[123]
c=a[20]
'''
for i in a:
    if(i[0] in user_id):
        try:
            all_data[str(i[1])]=all_data[str(i[1])]+1
        except:
            all_data[str(i[1])]=1

sorted_data=dict(sorted(all_data.items(), key=lambda x: x[1],reverse=True))
a=list(sorted_data.keys())
a=a[:500]
a.sort()
print(a)
    





'''
biggest=0

for i in a:
    if(i[0]>biggest):
        biggest=i[0]


print(biggest)        
'''