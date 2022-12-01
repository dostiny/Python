import sys; sys.stdin = open('input/flatten_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    while N+1 != 0:
        n = len(arr)
        max_v = 0
        max_idx = 0
        min_v = 101
        min_idx = 0
        for i in range(n):
            if max_v < arr[i]:
                max_v = arr[i]
                max_idx = i
            if min_v > arr[i]:
                min_v = arr[i]
                min_idx = i
        arr[max_idx], arr[min_idx] = max_v - 1, min_v + 1
        N -= 1
    result = max_v-min_v
    print(f'#{tc} {result}')