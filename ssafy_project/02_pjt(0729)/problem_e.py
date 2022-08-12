import requests
from pprint import pprint


def credits(title):
    search_url = f'https://api.themoviedb.org/3/search/movie?api_key=c6620f982d594e3c3ffac2ba88c0253f&language=ko-KR&query={title}&page=1&include_adult=false'
    response = requests.get(search_url).json()
    search_movie = response.get('results')
    searching = response.get('total_results')
    movie_id = 0
    if searching == 0:
        return None
    else:
        movie_id = search_movie[0].get('id')
    
    cast_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=c6620f982d594e3c3ffac2ba88c0253f&language=ko-KR'
    cast_total = requests.get(cast_URL).json()
    cast_catalog = cast_total.get('cast')
    crew_catalog = cast_total.get('crew')

    cast_list = [human.get('name') for human in cast_catalog if human.get('cast_id') < 10]
    direct_list = [direct.get('name') for direct in crew_catalog if direct.get('known_for_department') == 'Directing']
    directer = []
    for value in direct_list:
        if value not in directer:
            directer.append(value)

    return {'cast':cast_list, 'directing':directer}

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
