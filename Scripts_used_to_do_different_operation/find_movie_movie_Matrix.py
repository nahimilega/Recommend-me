
import numpy as np
import math
import csv

f = open("full_matrix_value.txt", "r")
full_matrix=[]
for x in f:
    if(x!='\n'):
        new=list(map(float,x.split(',')))
        
        full_matrix.append(new)

print(len(full_matrix))
print(len(full_matrix[2]))

def make_cosine_matrix(a,b):
    '''
    To do cosine sinalitity operation an

    '''
    
    mat1=np.array(a)
    mat2=np.array(b)
    #To iterate over the columns we will take the transpose
    #temp_mat1=np.transpose(mat1)
    i=0
    numrator=0
    
    while(i<len(a)):
        numrator+=mat1[i]*mat2[i]
        i+=1
            
    denominator=math.sqrt(np.dot(mat1,mat1)*np.dot(mat2,mat2))
    cosine_relation=numrator/denominator  
    
    return cosine_relation


  

full_matrix=np.transpose(full_matrix)

movie_movie_matrix=[]

for i in full_matrix:     #Iterationg over all the present users
    one_row=[]
    for j in full_matrix:    
        simalirity=make_cosine_matrix(j,i)
        one_row.append(simalirity)
        
    movie_movie_matrix.append(one_row)


print("hi")
with open('movie_movie.txt', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(movie_movie_matrix)
writeFile.close()
