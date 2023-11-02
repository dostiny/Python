day = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
for TC in range(1, int(input()) + 1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0

    if m1 == m2:
        result = d2 - d1 + 1
    else:
        result = day[m1] - d1 + 1 + d2
        for i in range(m1 + 1, m2):
            result += day[i]
    print(f'#{TC}', result)