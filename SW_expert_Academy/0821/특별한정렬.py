for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for _ in range(N):
        for i in range(N-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    n_arr = []
    for i in range(5):
        n_arr += [arr[N-1-i], arr[i]]
    print(f'#{tc}', *n_arr)