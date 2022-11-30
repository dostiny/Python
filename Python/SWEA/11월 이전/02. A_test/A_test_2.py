import sys; sys.stdin = open('input_2.txt')

def money_m():
    for j in range(N):
        for i in range(1, L + 1):
            money_li[j][i] = arr[j][i] - arr[j][i - 1]

def buy():
    global Ms, Ma
    for i in range(1, L + 1):
        if i >= 2:
            Ms += Ma
        max_v1 = max_v2 = 0
        idx1 = idx2 = -1
        for j in range(N):
            if 0 < money_li[j][i]:
                if max_v1 < money_li[j][i]:
                    max_v1, max_v2 = money_li[j][i], max_v1
                    idx1, idx2 = j, idx1
                elif max_v2 < money_li[j][i]:
                    max_v2 = money_li[j][i]
                    idx2 = j
        # print(1, i, Ms)
        if idx1 == -1 and idx2 == -1:
            pass
        elif idx2 == -1:
            a = Ms//arr[idx1][i-1]
            Ms -= arr[idx1][i-1] * a
            Ms += arr[idx1][i] * a
        else:
            a = Ms // arr[idx1][i-1]
            Ms -= arr[idx1][i-1] * a
            b = Ms // arr[idx2][i-1]
            Ms -= arr[idx2][i-1] * b
            Ms += arr[idx1][i] * a
            Ms += arr[idx2][i] * b
        # print(2, i, Ms)

for TC in range(1, int(input()) + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    MM = Ms + (Ma * L)
    arr = [list(map(int, input().split())) for _ in range(N)]
    money_li = [[0] * (L + 1) for _ in range(N)]

    money_m()
    buy()
    print(f'#{TC}', Ms - MM + Ma)