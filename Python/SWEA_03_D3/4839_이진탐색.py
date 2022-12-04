for TC in range(1, int(input()) + 1):
    P, A, B = map(int, input().split())
    la = lb = 1
    ra = rb = P
    result = 1
    while True:
        ca = (la + ra) // 2
        cb = (lb + rb) // 2
        if ca == A:
            result = 'A'
        else:
            if A < ca:
                ra = ca
            elif ca < A:
                la = ca
        if cb == B:
            if result != 'A':
                result = 'B'
            elif result == 'A':
                result = 0
        else:
            if B < cb:
                rb = cb
            elif cb < B:
                lb = cb
        if result != 1:
            break

    print(f'#{TC}', result)