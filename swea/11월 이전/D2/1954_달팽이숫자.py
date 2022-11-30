T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    nn = N**2
    start = 1
    ar, ac = 0, 0
    dirc = 3
    while start != nn:
        arr[ar][ac] = start
        if dirc == 0:
            ar, ac = ar - 1, ac
            if ar == 0 or arr[ar-1][ac] != 0:
                dirc = 3
        elif dirc == 1:
            ar, ac = ar + 1, ac
            if ar == N-1 or arr[ar+1][ac] != 0:
                dirc = 2
        elif dirc == 2:
            ar, ac = ar, ac - 1
            if ac == 0 or arr[ar][ac-1] != 0:
                dirc = 0
        elif dirc == 3:
            ar, ac = ar, ac + 1
            if ac == N-1 or arr[ar][ac+1] != 0:
                dirc = 1
        start += 1
        if start == nn:
            arr[ar][ac] = start
    print(f'#{test_case}')
    for ar in arr:
        print(*ar)