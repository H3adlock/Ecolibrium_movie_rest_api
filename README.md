# Ecolibrium_movie_rest_api
API for movie list like imdb

An API interface to create, update , delete and to search or find movies by names, directors.

It uses data from imdb.json to populate the initial Db

## Setting up project Linux
```
# create a virtualenv 
virtualenv env_movie
source env_movie/bin/activate
```
## Setting up project Windows
```
# create a virtualenv 
virtualenv env_movie
source env_movie\Scripts\activate
```
```
pip install -r reuqirements.txt
./manage.py migrate
./manage.py runserver
./manage.py load_dataset
```

##Demo
https://ecolibrium-movie.herokuapp.com/api/movies

#API request examples

### For Authentication
retrieve auth token by providing username and password in body
https://ecolibrium-movie.herokuapp.com/api-token-auth/

### For Anonymous Users
base API url
https://ecolibrium-movie.herokuapp.com/api/movies

filter by name (full text search)
https://ecolibrium-movie.herokuapp.com/api/movies?name=Star%20Wars

filter by movie name and director name
https://ecolibrium-movie.herokuapp.com/api/movies?name=Star%20Wars&director=George%20Lucas

detail view of a single movie only GET allowed
https://ecolibrium-movie.herokuapp.com/api/movies/details/244

### For Admin Users Only
add movie POST allowed for admin users only
https://ecolibrium-movie.herokuapp.com/api/movies/create

detail view of a single movie PUT,PATCH,DELETE allowed for admin users only
https://ecolibrium-movie.herokuapp.com/api/movies/details/244