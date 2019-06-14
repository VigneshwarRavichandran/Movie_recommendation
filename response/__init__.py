from rotten_tomatoes_client import *
import imdb

ia = imdb.IMDb()

def get_recommendation(movie_name):
  movie_search = ia.search_movie(movie_name)
  movie_id = movie_search[0].movieID
  movie = ia.get_movie(movie_id)
  genres = []
  for genre in movie['genres']:
    if genre == 'Action' or genre == 'Thriller' or genre == 'Crime' or genre == 'Reality-TV' or genre == 'Game-Show' or genre == 'War' or genre == 'Sport':
      genres.append(Genre.action)
    elif genre == 'Animation':
      genres.append(Genre.animation)
    elif genre == 'Comedy':
      genres.append(Genre.comedy)
    elif genre == 'Documentary' or genre == 'Biography' or genre == 'News':
      genres.append(Genre.documentary)
    elif genre == 'Drama' or genre == 'Western' or genre == 'Talk-Show' or genre == 'Short':
      genres.append(Genre.drama)
    elif genre == 'Family':
      genres.append(Genre.kids_and_family)
    elif genre == 'Horror':
      genres.append(Genre.horror)
    elif genre == 'Mystery' or genre == 'Adventure ':
      genres.append(Genre.mystery)
    elif genre == 'Fantasy' or genre == 'Sci-Fi':
      genres.append(Genre.sci_fi_and_fantasy)
    elif genre == 'Romance' or genre == 'Adult':
      genres.append(Genre.romance)
    elif genre == 'Film Noir' or genre == 'Musical' or genre == 'Music':
      genres.append(Genre.art_and_foreign)
    elif genre == 'History':
      genres.append(Genre.classics)

  query = MovieBrowsingQuery(minimum_rating=70, maximum_rating=100, certified_fresh=False, genres=genres, sort_by=SortBy.popularity, category=MovieBrowsingCategory.all_dvd_and_streaming)
  results = RottenTomatoesClient.browse_movies(query=query)
  response = []
  for result in results['results']:
    response.append(result['title'])
  return response