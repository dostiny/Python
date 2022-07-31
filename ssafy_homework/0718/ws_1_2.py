from functools import total_ordering


import math

total_post = int(input('게시글의 총 갯수를 입력하세요 : '))
page_post = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))

total_page = math.ceil(total_post/page_post)

print(total_page)