for TC in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    arr = []
    for i in range(1, H * W + 1):
        arr.append(i)
    print(f'#{TC}')
    for i in range(H):
        for j in range(W):
            print(arr[j], end=' ')
        print('')
        arr = arr[W:]