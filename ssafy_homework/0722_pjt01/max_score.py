data = [
    {'title' : '국어', 'score': 77},
    {'title' : '수학', 'score': 67},
    {'title' : '영어', 'score': 34},
    {'title' : '과학', 'score': 94},
    {'title' : '음악', 'score': 67},
    {'title' : '프로그래밍', 'score': 99},
    {'title' : '체육', 'score': 86}
]
max_score = 0
title = ''
for item in data:
    if max_score < item['score']:
        max_score = item['score']
        title = item['title']
print(max_score, title)
