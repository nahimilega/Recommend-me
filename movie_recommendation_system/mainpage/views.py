
# Create your views here.
from django.shortcuts import render,get_object_or_404
import pymongo

import numpy as np
import math
import json
from multiprocessing import Process # To call two function together
#User id and movie id starts from 0

 #Dictionary of movie_id reated by the user and their ratings


p=[]
q=[]
full_matrix=[]


#To connect to remote database 
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient("mongodb://admin:pass1234@cluster0-shard-00-00-qhthx.mongodb.net:27017,cluster0-shard-00-01-qhthx.mongodb.net:27017,cluster0-shard-00-02-qhthx.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb=myclient['movie_data'] 
maintable = mydb["mainpage_movielist"]
all_movies=maintable.find()  # It extracts all the movies from the database and show them. It is kept so that the request is called once and hence speed up the process


all_computed_matrixx=mydb["mainpage_all_computed_matrix"]
all_computed_matrix=all_computed_matrixx.find()

full_matrix=all_computed_matrix
temp_dict=all_computed_matrix[2]
full_matrix=temp_dict['user_rating']
full_matrix=np.array(json.loads(full_matrix))

temp_dict=all_computed_matrix[3]
movie_movie=temp_dict['movie_movie']
movie_movie_matrix=np.array(json.loads(movie_movie))


input_from_the_user={}

def form(request):
    '''
    This function is called when user lands in the mainpage of the website
    It displays all the movies in the database and ask user to rate those movies.
    At least 5 movies 
    Returns -
    all_movies : All the movies that are present in the database
    user_entries : No. of movies that the user has to rate to activate the recommendation process
    '''
    global input_from_the_user
    input_from_the_user.clear()
    all_movies=maintable.find() 
    return render(request,"mainpage/main.html",{'all_movies':all_movies,'user_entries': 5 - len(input_from_the_user) })


def store_data(request):
    '''
    This function is called when user submits the rating. 
    It takes rating through post request and stores it in the dictionary variable named input_from_the_user
    Returns -
    all_movies : All the movies that are present in the database
    user_entries : No. of movies that the user has to rate to activate the recommendation process
    current_rating : Dictionary containing movies the user has rated so far and their respective ratings
    movies_user_have_chosen : List of id of movies that the user has rated so far
    '''
    global input_from_the_user
    input_from_the_user[int(request.POST.get('rating[post_id]'))]=int(request.POST.get('rating[rating]'))
    input_movie_id=list(input_from_the_user.keys())
    input_movie_id= list(map(int, input_movie_id))
    all_movies=maintable.find()
    #input_from_the_user = {int(k):int(v) for k,v in input_from_the_user.items()}
    return render(request,"mainpage/main.html",{'all_movies':all_movies,'user_entries':5-len(input_from_the_user),'current_rating': input_from_the_user ,'movies_user_have_chosen':input_movie_id } )




def result(request):
    '''
    This function is executed when user presses the recommend button.It find the ids of movies which 
    match the taste of user based on the rating given by the user
    Returns-
    all_movies : Recommended movies for that particular user
    '''
    
    list_of_recommended_movies=recommend_a_movie(input_from_the_user)
    #print(list_of_recommended_movies)
    #data = maintable.find_one({'id': 20})
    search_query=[]
    for i in list_of_recommended_movies:
        a={'id':i}
        search_query.append(a)

    all_new_movies=maintable.find({"$or":search_query})  
    print(list_of_recommended_movies)
    print(input_from_the_user)
    return render(request,"mainpage/result.html",{'all_movies':all_new_movies,'user_entries':len(input_from_the_user) })


def recommend_a_movie(input_from_the_user):
    '''
    This funtion is used to find the movie ids og the movie that the user could like based 
    on the recommendations filled by the user  
    Parameters-
    input_from_the_user - dictionary of the movies the user has rated and their respective ratings
    Returns-
    The list of movie ids that are most suited for the user
    '''
    list_of_rated_movies_by_new_user = list(input_from_the_user.keys())
    full_matrix2=np.transpose(full_matrix) 
    length=len(full_matrix2)
    i=0                     #To cahnge
    user_rating_matrix_of_selected_movies=[]
    full_matrix2=list(full_matrix2)
    while(i<length):        
        if(i in list_of_rated_movies_by_new_user):    #We need to iterate over movies so we work of the transposed matrix of user rating       
            user_rating_matrix_of_selected_movies.append(full_matrix2[i])
        i+=1    
    
    user_rating_matrix_of_selected_movies=np.transpose(user_rating_matrix_of_selected_movies) #This is the matrix of all the user ration for those movies which are rated by user   
    new_user_rating=list(input_from_the_user.values())

    simalirity_dict={}      #Recored simalirity of each user with respect to the new user 
    count=0                 #This is made to maintain the count of userid
    for i in user_rating_matrix_of_selected_movies:     #Iterationg over all the present users to find user user simalirity    
        simalirity=make_cosine_matrix(new_user_rating,i)
        simalirity_dict[str(count)]=simalirity
        count+=1

    potential_rating_of_new_user=most_similar_user(simalirity_dict,input_from_the_user) 
    #To sort dictionary on the bases of values
    
    
    
    return potential_rating_of_new_user







def make_cosine_matrix(a,b):
    '''
    This function takes in two list and find the cosine simalirity between both the list
    Parameters-
    a = First list to compute cosine simalirity
    b = Second list to compute cosine simalirity
    Returns-

    cosine_relation : Cosine simalirity between both the list

    '''  
    mat1=np.array(a)
    mat2=np.array(b)
    i=0
    numrator=0   
    while(i<len(a)):
        numrator+=mat1[i]*mat2[i]
        i+=1          
    denominator=math.sqrt(np.dot(mat1,mat1)*np.dot(mat2,mat2))
    cosine_relation=numrator/denominator   
    return cosine_relation


def item_item_filter(input_from_the_user):
    '''
    This function implements item-item filter.It uses the movie-movie relation matrix that is present in the database 
    and use it to find most similar movies to the movies the user has entered.  
    Returns-
    recommended_movie_ids - A list of movie ids that are recommende to the user
    '''
    
    global movie_movie_matrix # to do 
    movie_id_of_movie_user_has_rated=list(input_from_the_user.keys())
    rating_from_the_user=list(input_from_the_user.values())
    dict_of_recommended_movies={}
    i=0
    while(i<len(rating_from_the_user)):
        if(rating_from_the_user[i]>3): #Because we don't want to find movies similar to the movies used don't like.
            current_movie_row=movie_movie_matrix[movie_id_of_movie_user_has_rated[i]]
            j=0
            while(j<len(current_movie_row)):
                if(current_movie_row[j]>0.7): #If simalirity between movie is greater that 0.7 Then it gets gets stored by multiplying the rating the user gave
                    dict_of_recommended_movies[j]=j*rating_from_the_user[i]
                j+=1
        i+=1 

    #To sort the dictionary on the bases on their values               
    sorted_recomended_movies=dict(sorted(dict_of_recommended_movies.items(), key=lambda x: x[1],reverse=True))
    recommended_movie_ids=list(sorted_recomended_movies.keys())
    
    return recommended_movie_ids


def most_popular_movies():
    '''
    This function is used to get id of most popular movies in the database according to imdb
    Returns-
    A list of id of most popular movies
    '''
    a=[497, 496, 494, 492, 490, 485, 480, 465, 464, 458, 447, 443, 441, 439, 413, 412, 409, 406, 405, 388, 386, 377, 371, 354, 328, 313]
    return a


    
def most_similar_user(simalirity_dict,input_from_the_user):
    '''

    This functions computes the list of movies that will be suitable for user on the bases of simalirity dictionary
    and if the simalirity with any user is not found then it recommend the movie on the bases of item item filter
    Returns-
    The list of recommended movie ids 
        
    '''
    # To sort the dictionary
    sorted_dict=dict(sorted(simalirity_dict.items(), key=lambda x: x[1],reverse=True))
    list_of_all_the_simalirities=list(sorted_dict.values())

    if(list_of_all_the_simalirities[0]>=0.8):   # List is sorted in reverse fashion so first index will hold the largest value
        count=0
        for i in list_of_all_the_simalirities:
            #The list is sorted so i am going to exploit that feature for my benifit
            if i<0.8 :  #reason for this number
                return all_most_related_users(sorted_dict,count)
            count+=1
        return all_most_related_users(sorted_dict,count)   # If all greater than 0.8
    else:        
        #Item item filter goes here
        #It finds related movies(with rating>3) + top movies(keep some of them on the bases of imdb rating)
        
        list_of_recommended_movies_through_itemfilter=item_item_filter(input_from_the_user)
        list_of_most_popular_movies=most_popular_movies()
        try:
        	p1 = Process(target=run_gradient_decent(input_from_the_user))
        	p1.start()
        finally:
        	if(len(list_of_recommended_movies_through_itemfilter)<15):
        		list_of_recommended_movies=list_of_recommended_movies_through_itemfilter
                list_of_recommended_movies.extend(list_of_most_popular_movies[:(20-len(list_of_recommended_movies_through_itemfilter))])
            else:
                list_of_recommended_movies=list_of_recommended_movies_through_itemfilter[:15]
                list_of_recommended_movies.extend(list_of_most_popular_movies[:5])

        return list_of_recommended_movies


def all_most_related_users(sorted_dict_of_users,count):			
    '''
    It takes the rating of most similar users and mean their rating and the show it 
    and returns the list of movies
    Returns
    List of recommended movie ids
    '''
    most_matched_users_list=list(sorted_dict_of_users.keys())

    most_matched_users_list=list(map(int,most_matched_users_list))[:5]
    #To change
    matrix_of_matched_users_and_movie_rating=[]
    length=len(full_matrix)
    i=0
    while(i<length):
        if(i in most_matched_users_list):
            matrix_of_matched_users_and_movie_rating.append(full_matrix[i])
        i+=1    

    
    x=np.array(matrix_of_matched_users_and_movie_rating)         #user rating matrix of most related users and all movies

    sum_of_rating_of_all_movies_for_selected_user=x.sum(axis=0, dtype='float')
    mean_of_rating_of_all_movies_for_selected_user=sum_of_rating_of_all_movies_for_selected_user/count	
    dict_of_all_movierating_of_new_user = dict(enumerate(mean_of_rating_of_all_movies_for_selected_user.flatten(), 0)) #movie_id starts from 1 
    
    sorted_potential_rating_of_new_user=dict(sorted(dict_of_all_movierating_of_new_user.items(), key=lambda x: x[1],reverse=True))
    sorted_list_of_movies_to_recommend=list(sorted_potential_rating_of_new_user.keys())[:20]
    return sorted_list_of_movies_to_recommend



#This section is for gradient desent this is envoked after item item filter(ie system encounters new user)
# So for future references and to improve the database gradient desent is ran on the ratings of that user to predict all other ratings and then it is stored in database

def run_gradient_decent(input_from_the_user):
    '''
    This function runs gradient desent and updates the database with new matrix

    '''
    a=np.zeros(499)
    for i in list(input_from_the_user.keys()):
        a[i]=input_from_the_user[str[i]]
    P = np.random.rand(1,10)
    Q = np.random.rand(499,10)  
    P,q,full=gradient_desent(a,P,Q)
    old=full_matrix
    full_matrix.append(full)
    
    
    myquery = { "user_rating": json.dumps(old.tolist()) }
    newvalues = { "$set": { "user_rating": json.dumps(full_matrix.tolist()) } }

    all_computed_matrixx.update_one(myquery, newvalues)

    



def gradient_desent(full_matrix, P, Q, K=10, iteration=1600, alpha=0.0015, beta=0.01):
    '''
    This function uses gradient desent technique to fill the empty boxes in full user rating matrix
    and breaks the matrises into two different matrix P and Q
    full_matrix=P*Qtranspose
    Paremeters-

    '''
    Q = Q.T# To take transpose
    for iterate in range(iteration):
        for i in range(len(full_matrix)):
            for j in range(len(full_matrix[i])):
                
                if full_matrix[i][j] > 0: 
                    
                    eij = full_matrix[i][j] - np.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])


        
        e = 0
        for i in range(len(full_matrix)):
            for j in range(len(full_matrix[i])):
                
                if full_matrix[i][j] > 0:
                    e = e + pow(full_matrix[i][j] - np.dot(P[i,:],Q[:,j]), 2)   #TO find rms error
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        
        if (iterate+1) % 10 == 0:                     #This will display after 10 itrations
                print("Iteration: " + str(iteration) +"error "+ str(e))
        if e < 0.001:
            break
    full_matrix=numpy.matmul(P,Q.T)        
    return (P, Q.T,full_matrix)