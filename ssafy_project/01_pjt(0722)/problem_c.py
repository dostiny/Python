import json
from pprint import pprint

def movie_info(movies, genres):
    movies_data = []

    for movie in range(len(movies)):
        data_id = []

        id = movies[movie].get('genre_ids')
        for num1 in id:
            for num2 in range(len(genres)):
                if num1 == genres[num2].get('id'):
                    data_id.append(genres[num2].get('name'))

        data = {
        'genre_ids': data_id,
        'id': movies[movie].get('id'),
        'overview': movies[movie].get('overview'),
        'poster_path': movies[movie].get('poster_path'),
        'title': movies[movie].get('title'),
        'vote_average': movies[movie].get('vote_average'),
        }
        movies_data.append(data)

    return movies_data
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
