T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    S = []
    top = -1
    sum_v = 0
    for i in arr:
        if i == 0:
            S.pop()
            top -= 1
        else:
            top += 1
            S.append(i)
    for i in S:
        sum_v += i
    print(f'#{test_case} {sum_v}')