##  1. Print the top director with maximum number of movies.

import json

def read_json_file(file_name):
    with open(file_name) as json_file:
        imdb_movie_data = json.load(json_file)
        return imdb_movie_data
    
def top_dir_with_max_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    dir = {}
    for i in imdb_movie_data:
        director = i['director']
        if director in dir:
            dir[director] += 1
        else:
            dir[director] = 1
    return dir
top_dir = top_dir_with_max_movies('assignment2/imdb_movies.json')
top_director = max(top_dir.items(),key=lambda x: x[1])
print(f"the top director is {top_director[0]} and his movie are {top_director[1]}")


##  2. Print the popular genere watched by most of the audiance.

def popular_genere_watched_by_most(file_name):
    imdb_movie_data = read_json_file(file_name)
    d = {}
    for i in imdb_movie_data:
        genere = i["genre"]
        if tuple(genere) in d:
            d[tuple(genere)] += 1
        else:
            d[tuple(genere)] = 1
    return d

top_genere_watched = popular_genere_watched_by_most('assignment2/imdb_movies.json')
top_genere_watched = max(top_genere_watched.items(),key=lambda x: x[1])
print(f"The popular genere watched by audiance is {top_genere_watched}")


## 3. Print out the top ten movies, according to imdb score.

def get_top_ten_movies_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    sorted_movies = sorted(imdb_movie_data, key=lambda x: x['imdb_score'], reverse=True)
    top_10_movies = sorted_movies[:10]
    return top_10_movies
top_movies = get_top_ten_movies_by_imdb_score('assignment2/imdb_movies.json')
for movie in top_movies:
    print(f"Movie: {movie['name']} with IMDb score: {movie['imdb_score']}")


##   4. Print the least watched movie based on their imdb score.

def least_watched_movie_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    d ={}
    for i in imdb_movie_data:
        movie_name = i["name"]
        d[movie_name] = i["imdb_score"]
    return d

least_watched_movie_imdb_score = least_watched_movie_by_imdb_score('assignment2/imdb_movies.json')
least_watched_movie_imdb_score = min(least_watched_movie_imdb_score.items(),key = lambda x:x[1])

print(f"the least watched movie based on their imdb score is : {least_watched_movie_imdb_score}")



##   5. Print the best director in the first hundred movies.


def get_best_director_in_first_hundred_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    d = {}
    for movie in imdb_movie_data:
        director = movie["director"]
        d[director] = movie["imdb_score"]
    return d
best_director_in_hundred_movies = get_best_director_in_first_hundred_movies('assignment2/imdb_movies.json')
best_director_in_hundred_movies= sorted(best_director_in_hundred_movies, key=lambda x: x[1], reverse=True)
best_director_in_hundred_movies = best_director_in_hundred_movies[:100]
best_director_in_hundred_movies = max(best_director_in_hundred_movies, key=lambda x: x[1])
print(f"the best director in first hundred movies is : {best_director_in_hundred_movies}")
    