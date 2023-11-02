def tsn(s, e):
    cnt = 0
    for i in range(s, e+1):
        if i % 3 == 0:
            cnt += 1
        else :
            for j in str(i):
                if j == '3' or j == '6' or j == '9':
                    cnt += 1
    return cnt

a, b = map(int, input().split())
print(tsn(a, b))