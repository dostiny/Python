import json


def dec_movies(movies):
    passrelease_lst = []
    passrelease = []

    for num in range(len(movies)):
        passrelease_lst.append(movies[num].get('id'))

    for num2 in passrelease_lst:
        movie_json = open(f'data/movies/{num2}.json', encoding='utf-8')
        movie_list = json.load(movie_json)
        movie = movie_list.get('release_date')
        if '12' == movie[5:7]:
            passrelease.append(movie_list.get('title'))
    return passrelease
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
