
user_rating_matrix_of_selected_movies=[]


new_user_rating=[]


def make_cosine_matrix(a,b):
	print(a)
	print(b)
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




    
simalirity_dict={}
count=0
for i in user_rating_matrix_of_selected_movies:
	print(count)
	simalirity=make_cosine_matrix(i,new_user_rating)
	simalirity_dict[str(count)]=simalirity
	count+=1

def most_similar_user(simalirity_dict):
	'''
	Returns his row of preference 
		
	'''
	sorted_dict=dict(sorted(simalirity_dict.items(), key=lambda x: x[1],reverse=True))
	list_of_all_the_simalirities=list(sorted_dict.values())
	if(top_k>=0.7):
		count=0
		for i in list_of_all_the_simalirities:
			#The list is sorted so i am going to exploit that feature for my benifit
			if i<0.7 :
				return all_most_related_users(sorted_dict,count)
				

			count+=1
	else:
		#Item item filter goes here
		related movies + top movies(keep some of them on the bases of imdb rating)



def all_most_related_users(list_of_all_the_simalirities,count)			
	'''
	It gets user rating matrix of those particular users only
	'''
	x=np matrix


	sum_of_rating_of_all_movies_for_selected_user=x.sum(axis=0, dtype='float')
	mean_of_rating_of_all_movies_for_selected_user=sum_of_rating_of_all_movies_for_selected_user/count	

	return mean_of_rating_of_all_movies_for_selected_user



potential_rating_of_new_user=most_similar_user()


