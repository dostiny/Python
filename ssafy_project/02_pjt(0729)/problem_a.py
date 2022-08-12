import requests

def popular_count():
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=c6620f982d594e3c3ffac2ba88c0253f&language=ko-KR%20&page=1'
    response = requests.get(URL).json()
    top_list = response.get('results')
    top_movies = 0
    for movie in top_list: # movie 는 딕셔너리 형태임
        top_movies += 1
    return top_movies
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    
    print(popular_count())
    # 20
