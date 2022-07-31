s_triangle = map(int, input().split())

a, b, c = s_triangle

if a == b and b == c:
    print('정삼각형')
elif a == b or a == c or b == c:
    if a ** 2 + b ** 2 == c ** 2:
        print('직각이등변삼각형')
    elif a ** 2 + c ** 2 == b ** 2:
        print('직각이등변삼각형')
    elif b ** 2 + c ** 2 == a ** 2:
        print('직각이등변삼각형')
    else:
        print('이등변삼각형')
elif a != b and a != c and b != c:
    if a ** 2 + b ** 2 == c ** 2:
        print('직각삼각형')
    elif a ** 2 + c ** 2 == b ** 2:
        print('직각삼각형')
    elif b ** 2 + c ** 2 == a ** 2:
        print('직각삼각형')
    else:
        print('삼각형')
        
else :
    print('삼각형이 아닙니다.')