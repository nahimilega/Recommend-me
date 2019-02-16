# Recommend Me

This is a movie recommendation system that recommends movie based on the ratings givev by the user. 
It uses Django for its backend
This is the code of webite hosted on this link- 
https://movie-watch-time.herokuapp.com/mainpage/form

<br>

# Description of the project

This website uses user-user collaborative filter, item-item collaborative filter and matrix factorization technique through gradient desent to recommend movies to the user. <br>
**Note** - numpy and pandas are __only used for data loading and doing some basic computations__ like matrix multiplication. All the algorithms are __implemented from scratch__ without use of any special library.<br>
<br>
### Whats happening behind the scene
Whenever a user lands on the website, he has to rate 5 movies. When he submit the rating his/her ratings are __compared with the rating of all the users(there are 500 of them)__ in the database for those particular movies and find the simalirity using __consine simairity.__ If the simalirity is above certain threshold then it takes the __mean of top k users__ that are most similar and recommend the movie accordingly.
<br>
If the simalirity is not found then __item-item filter is activated__ and returns the movies related to the movies that are liked by the user and some __top movies which have highest imdb rating__ in the database.And after recommending to the user the program __runs gradient decent__ on the new rating recieved and store them in database for future reference.
<br>
<br>
<br>
The ratings of the user are taken from Movielens2M dataset and matrix factorization eas ran on the initial user rating matrix to fill in all the boxs of the matrix<br>
For optimum performnace and to get a dense matrix the movies(there are 499 of them in database) that were most rated by the users are taken from the 2M dataset.This will also ensure that __movies in the databse are the popular one__ and majority of users know some of them<br>

<br>





## Installation

Download this repository

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies of this project

```bash
pip install -r requirements.txt
```

## Usage

To run the website on the local host
```bash
cd movie_recommendation_system
python manage.py runserver

```
Now open your web browser on paste the following url 

```
http://127.0.0.1:8000/mainpage/form
```


# Roadmap

##### movie-recommendation-system :
This is the folder where Django website resides. All the frontend and backend <br>
##### Scripts_used_to_do_different_operation :
This folder contains all the python script that I used to do diffferent operations ranging from applying gradient decent on inital matrix to selecting top 500 movies from 2M movies and a lot more all the way to script used to check if movies of all genre is present in database.<br>
#### modified_dataset : 
The csv files of original dataset were huge and difficult to work with so to ease up the process I extracted only the useful information from the whole dataset and stored it in this folder. Unfortunately due to restriction of github of file size I could not upload all the files.<br>
#### txt_files :
This folder contains some txt files which were used to store data for testing purposes.<br>



# Sources of reference <br />
### Template used for frontend
https://www.templatemonster.com/website-templates/57969.html
### Dataset-
Movie lens 2M dataset<br />

### Other references-
StackOverflow<br />
https://towardsdatascience.com/various-implementations-of-collaborative-filtering-100385c6dfe0<br />
https://github.com/yanneta/pytorch-tutorials/blob/master/collaborative-filtering-nn.ipynb<br />
https://medium.com/@james_aka_yale/the-4-recommendation-engines-that-can-predict-your-movie-tastes-bbec857b8223<br />
https://beckernick.github.io/matrix-factorization-recommender/<br />
https://medium.com/@cfpinela/recommender-systems-user-based-and-item-based-collaborative-filtering-5d5f375a127f<br />
https://towardsdatascience.com/collaborative-filtering-based-recommendation-systems-exemplified-ecbffe1c20b1<br />
https://medium.com/@connectwithghosh/simple-matrix-factorization-example-on-the-movielens-dataset-using-pyspark-9b7e3f567536<br />
https://github.com/khanhnamle1994/movielens<br />
http://www.albertauyeung.com/post/python-matrix-factorization/<br />
https://stackoverflow.com/questions/52993954/how-to-store-np-arrays-into-psql-database-and-django<br />
https://docs.scipy.org/doc/numpy-1.15.0/<br />
