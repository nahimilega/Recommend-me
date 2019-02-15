
import urllib.request

from time import sleep

from bs4 import BeautifulSoup
import pymongo
import pandas as pd


#csv.register_dialect('myDialect',delimiter = ',',skipinitialspace=True)


'''
with open('new_links.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        file.append(row)

csvFile.close()
'''
df = pd.read_csv("new_links.csv")

file=df.to_numpy()




'''
for i in range(1,500):
    print(int(file[i][0]))


temp=[1,2,3]
print(temp[9])
'''


def make_imdb_link(imdb_id):
    '''

    '''
    
    imdb_id=str(int(imdb_id))
    while(len(imdb_id)<7):              #To standarsize all ids to 7 digits
        imdb_id='0'+imdb_id

    final_url='https://www.imdb.com/title/tt'+imdb_id+ '/'
    
    return final_url

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient['movie_data'] 
maintable = mydb["mainpage_movielist"]


for bigger_loop in range(len(file)):
    url_of_movie=make_imdb_link(file[bigger_loop][1])
    print(url_of_movie)
    req = urllib.request.Request(url_of_movie)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    genre=''
    imdb=0
    sypnosis=''
    img=''
    name=''
    year=0
    soup = BeautifulSoup(the_page, 'html.parser')

    imdb_raw=soup.find('span', attrs={'itemprop':'ratingValue'})
    imdb=imdb_raw.text.strip()

    year_raw=soup.find('span', attrs={'id':'titleYear'})
    year=year_raw.text.strip()[1:-1]
    #print(year)

    name_year_raw=soup('div', attrs={'class':'title_wrapper'})          #ginding name is dependent on year
    name_year=name_year_raw[0].text.strip()
    index_of_the_year_in_the_text=name_year.find(year)
    name=name_year[:index_of_the_year_in_the_text-2]
    #print(name)
    try:             
        img_raw=soup.find('div', attrs={'class':'poster'})
        image=img_raw.img
        image_link=image['src']
    except:
        image_link=''    
    #print(image_link)
    soup_for_genre=BeautifulSoup(str(soup.find('div', attrs={'class':'subtext'})),'html.parser')
    genre_raw=soup_for_genre.find_all('a')
    for i in range(len(genre_raw)-1):       #To remove release date
        genre+=str(genre_raw[i].text.strip())+","
    genre=genre[:-1] # to remove comma in the end
    sypnosis_raw=soup.find('div', attrs={'class':'summary_text'})
    sypnosis=sypnosis_raw.text.strip()
    #print(sypnosis)

    print(int(file[bigger_loop][0]))

    '''
    This part is for storing in database
    '''
    

    mydict = { 'id':int(bigger_loop),'movielensid':int(file[bigger_loop][0]),"movie_name": str(name), "thumbnail": str(image_link),"imdb": str(imdb),"imbd_link":str(url_of_movie) ,"genre":str(genre),"year":int(year),"sypnosis":str(sypnosis) }
    maintable.insert_one(mydict)





#img_raw=soup('img', attrs={'class':'loadlate'})

#img.append(img_raw[0]['loadlate'])

"""

while (i<len(box_without_post_production)):
    temp_soup = BeautifulSoup(str(box_without_post_production[i]), 'html.parser')

    genre_raw = temp_soup('span', attrs={'class': 'genre'})
    genre.append(genre_raw[0].text.strip())

    imdb_raw=soup('div', attrs={'class':'inline-block ratings-imdb-rating'})
    imdb.append(imdb_raw[i].text.strip())

    sypnosis_raw=temp_soup('p', attrs={'class':'text-muted'})
    sypnosis.append(sypnosis_raw[1].text.strip())

    img_raw=temp_soup('img', attrs={'class':'loadlate'})
    name.append(img_raw[0]['alt'])
    img.append(img_raw[0]['loadlate'])

    year_raw=temp_soup('span', attrs={'class':'lister-item-year text-muted unbold'})
    year.append(year_raw[0].text.strip())
    
    i+=1    

"""

'''
imdb final
metascore final
sypnosis final
name final
image final
year final

i=1
while(i<len(sypnosis_raw)):
    
    i+=2
print(sypnosis)  

imdb done
gener done
meta_score done
sypnosis done 
name done
img done
'''




'''
box=soup('div', attrs={'class':'lister-item mode-advanced'})
box_without_post_production=box
meta_score=[]
i=0

while (i<len(box)):
    temp_soup = BeautifulSoup(str(box[i]), 'html.parser')

    try:
        meta_score_raw=temp_soup('div', attrs={'class':'inline-block ratings-metascore'})
        meta_score.append(meta_score_raw[0].text.strip())
        i+=1
    except:
        del box_without_post_production[i]
        i+=1
        pass   
#print(meta_score)   
genre=[]
imdb=[]
sypnosis=[]
img=[]
i=0
name=[]
year=[]
'''