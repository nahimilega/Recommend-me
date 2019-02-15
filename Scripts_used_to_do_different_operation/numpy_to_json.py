import json
import numpy as np
f = open("p_value.txt", "r")
final_matrix=[]
for x in f:
    if(x!='\n'):
        new=list(map(float,x.split(',')))
        
        final_matrix.append(new)


 # a 2 by 5 array

arrr=np.array(final_matrix) 
b = arrr.tolist() 
aaa=json.dumps(b)
print(type(aaa))

'''
a=np.array(final_matrix)

dic=json.dumps(a.tolist())

print(type(dic))

divv={3:2,6:2,64:2}
print(type(divv))
'''