import sys; sys.stdin = open('1210.txt', 'r')


for tc in range(1, 11):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착점 ==> 출발점
    r = c = 0
    for i in range(100): # 99번행(마지막)을 조사
        if ladder[99][i] == 2:
            r, c = 99, i
            break

    while r: # 반복해서 한칸씩 이동,
        # 내가 지나온 길은 풀 한포기도 남기지 않겠다. 따흐..
        ladder[r][c] = 0
        if c > 0 and ladder[r][c - 1]: # 길이 있다면 좌로 이동
            c -= 1
        elif c + 1 < 100 and ladder[r][c + 1]: # 길이 있다면 우로 이동
            c += 1
        else:                           # 위로 이동
            r -= 1

    print(c)