for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_idx = min_idx = 0
    max_v = 0
    min_v = 10
    for i in range(N):
        if max_v <= arr[i]:
            max_v = arr[i]
            max_idx = i
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i
    if max_idx > min_idx:
        result = max_idx - min_idx
    else:
        result = min_idx - max_idx
    print(f'#{tc} {result}')