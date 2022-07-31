import json
from pprint import pprint


def movie_info(movie, genres):
    data_id = []
    
    id = movie.get('genre_ids')
    for num1 in id:
        for num2 in range(len(genres)):
            if num1 == genres[num2].get('id'):
                data_id.append(genres[num2].get('name'))
    
    data = {
    'genre_ids': data_id,
    'id': movie.get('id'),
    'overview': movie.get('overview'),
    'poster_path': movie.get('poster_path'),
    'title': movie.get('title'),
    'vote_average': movie.get('vote_average'),
    }

    return data
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
