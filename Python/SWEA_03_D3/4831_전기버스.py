for TC in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    stop = [0] * (N + 1)
    for i in arr:
        stop[i] = 1
    bus, cnt = 0, 0
    while bus <= N:
        busno = 0
        for i in range(K):
            bus += 1
            if bus <= N and stop[bus] == 1:
                pass
            elif bus > N:
                break
            else:
                busno += 1
        if busno == K:
            cnt = 0
        else:
            cnt += 1
    print(cnt)