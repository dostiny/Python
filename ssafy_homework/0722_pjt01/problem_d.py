import json


def max_revenue(movies):
    movie_id = []
    revenue_lst = []

    for movie in movies:
        movie_id.append(movie['id'])

    for num2 in movie_id:
        movie_json = open(f'data/movies/{num2}.json', encoding='utf-8')
        movie_list = json.load(movie_json)
        revenue_lst.append((movie_list.get('revenue'),movie_list.get('id')))
    
    revenue_lst.sort(reverse=True)
    top = revenue_lst[0][1]
    for i in movies:
        if i['id'] == top:
            return i.get('title')
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
