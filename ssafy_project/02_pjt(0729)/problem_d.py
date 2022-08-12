import requests
from pprint import pprint


def recommendation(title):
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key=c6620f982d594e3c3ffac2ba88c0253f&language=ko-KR&query={title}&page=1&include_adult=false'
    response = requests.get(search_url).json()
    search_movie = response.get('results')
    searching = response.get('total_results')
    movie_id = 0
    if searching == 0:  # 한줄 if 문을 해보려고 시도
        return None
    else:
        movie_id = search_movie[0].get('id')

    recommend_url = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=c6620f982d594e3c3ffac2ba88c0253f&language=ko-KR&page=1'
    recommend_response = requests.get(recommend_url).json()
    recommend_dict = recommend_response.get('results')
    recommend_list = [recommend.get('title') for recommend in recommend_dict]
    return recommend_list
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
