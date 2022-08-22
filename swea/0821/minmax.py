import sys; sys.stdin = open('input/minmax.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    min_v = 1000001
    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]
    result = max_v - min_v
    print(f'#{tc} {result}')