f = open("movie_movie.txt", "r")
final_matrix=[]
for x in f:
    if(x!='\n'):
        new=list(map(float,x.split(',')))
        
        final_matrix.append(new)




    
#print(final_matrix)
print(len(final_matrix))
print(len(final_matrix[1]))