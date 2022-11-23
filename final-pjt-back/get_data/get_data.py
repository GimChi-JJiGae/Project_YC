import urllib.request
from pprint import pprint
import json

API_KEY = "5d2592924ae354925561438e12ee8888"
HOST = "https://api.themoviedb.org"
MOVIE_LIST_URI = "/3/movie/popular"
MOVIE_INFO_URI = "/3/movie/"
GENRE_LIST_URI = "/3/genre/movie/list"

movie_list = []
movie_Ids = []
genre_list = []
print("check")
genre_request = (f'{HOST}{GENRE_LIST_URI}?api_key={API_KEY}&language=ko')
response = urllib.request.urlopen(genre_request)
json_str = response.read().decode('utf-8')
json_object = json.loads(json_str)
print("check")
genre_data = json_object.get("genres")
print("check")
for data in genre_data:

    my_data = {
        "number": data.get("id"),
        "name": data.get("name")
    }
    print("check")
    my_genre = {
        "model": "movies.genre",
        "pk": my_data.get("number"),
        "fields": {
            "name": my_data.get("name")
        },
    }
    genre_list.append(my_genre)
print("check")
for i in range(1, 50):
    request = (f'{HOST}{MOVIE_LIST_URI}?api_key={API_KEY}&language=ko&page={i}')
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)

    data_movies = (json_object.get("results"))

    for movie in data_movies:
        movie_Ids.append(movie.get("id"))

for idx, movie_Id in enumerate(movie_Ids):
    print(f'{idx}')
    movie_request = (f'{HOST}{MOVIE_INFO_URI}{movie_Id}?api_key={API_KEY}&language=ko&')
    response = urllib.request.urlopen(movie_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)
    if json_object.get("poster_path"):
        if json_object.get("genres"):
            genre_orginal_data = json_object.get("genres")
            genre_id_list = []
            for i in genre_orginal_data:
                genre_id_list.append(i['id'])
            my_object = {
                "model": "movies.movie",
                "pk": idx+1,
                "fields": {
                    "title": json_object.get("title"),
                    "adult": json_object.get("adult"),
                    "popularity": json_object.get("popularity"),
                    "poster_path": json_object.get("poster_path"),
                    "release_date": json_object.get("release_date"),
                    "runtime": json_object.get("runtime"),
                    "vote_average": json_object.get("vote_average"),
                    "vote_count": json_object.get("vote_count"),
                    "overview": json_object.get("overview"),
                    "genres": genre_id_list,#json_object.get("genres"),
                    "original_title": json_object.get("original_title"),

                    "original_id": json_object.get("id"),
                }  
            }
        else:
            genre_orginal_data = json_object.get("genres")
            genre_id_list = []
            for i in genre_orginal_data:
                genre_id_list.append(i['id'])
            my_object = {
                "model": "movies.movie",
                "pk": idx+1,
                "fields": {
                    "title": json_object.get("title"),
                    "adult": json_object.get("adult"),
                    "popularity": json_object.get("popularity"),
                    "poster_path": json_object.get("poster_path"),
                    "release_date": json_object.get("release_date"),
                    "runtime": json_object.get("runtime"),
                    "vote_average": json_object.get("vote_average"),
                    "vote_count": json_object.get("vote_count"),
                    "overview": json_object.get("overview"),
                    "genres": genre_id_list,#json_object.get("genres"),
                    "original_title": json_object.get("original_title"),

                    "original_id": json_object.get("id")


                }
            }
        movie_list.append(my_object)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_list, ensure_ascii=False))

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False))
