for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())
    box = [0] * N
    cnt = 1

    for _ in range(Q):
        L, R = map(int, input().split())
        for i in range(L-1, R):
            box[i] = cnt
        cnt += 1
    print(f'#{tc}', *box)
