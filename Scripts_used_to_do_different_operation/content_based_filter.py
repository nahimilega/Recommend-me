import pandas as pd
import numpy as np
import math

def make_cosine_matrix(a,b):
    mat1=np.array(a)
    mat2=np.array(b)
    cosine_matrix=[]
    #To iterate over the columns we will take the transpose
    temp_mat1=np.transpose(mat1)
    for i in temp_mat1:
        one_row=[]
        for j in mat2:
            dot_product=np.dot(i,j)
            denominator=math.sqrt(np.dot(i,i)*np.dot(j,j))
            cosine_relation=dot_product/denominator
            one_row.append(cosine_relation)
        
        cosine_matrix.append(one_row)    

    return cosine_matrix

df = pd.read_csv("new_genome-score.csv")
a=df.to_numpy()
all_data={}
user_id=[]
#1128
'''
To extract the data from the file and make it something meaningful
'''
final_matrix=[]
onerow=[]
for i in a:
    onerow.append(i[2])

    if(i[1]==1128):
        final_matrix.append(onerow)
        onerow=[]

final=np.array(final_matrix)
transposed_final=np.transpose(final)
matt=make_cosine_matrix(transposed_final,final)
fin_mat=np.array(matt)
print(fin_mat)
print(fin_mat.shape)

