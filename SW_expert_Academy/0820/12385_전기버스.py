import sys; sys.stdin = open('input/12385_input.txt', 'r')

for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    stop = [0] + list(map(int, input().split())) + [N]

    bus = 0
    cnt = 0
    for i in range(1, M+2):
        if stop[i] - stop[i-1] > K:
            cnt = 0
            break
        elif bus + K < stop[i]:
            bus = stop[i-1]
            cnt += 1
    print(f'#{tc} {cnt}')