from movie_model import MovieModeler
import requests

def MovieApi():
    url = f'''
      https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
    '''
    response = requests.get(url)

    responseDoct = response.json() 
    movies = responseDoct["title"]["rating"]["small_cover_image"]["summary"] 
    return convart_model(movies)


def convart_model(movies):
    list = []

    for movie in movies:
        movie_model = MovieModeler(
            movie["title"],
            movie["rating"],
            movie["small_cover_image"],
            movie["summary"]
        )
        list.append(movie_model)

    print(list)
    return list