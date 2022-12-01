for TC in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = (sorted(list(set(map(int, input().split())))))
    print(f'#{TC}', arr[K - 1])