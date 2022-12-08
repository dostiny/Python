for TC in range(1, int(input()) + 1):
    str1 = list(input())
    N = len(str1)
    str2 = list(input())
    numst = [0] * N
    max_v = 0
    for i in range(N):
        for j in str2:
            if str1[i] == j:
                numst[i] += 1
        if max_v < numst[i]:
            max_v = numst[i]
    print(f'#{TC}', max_v)