import sys; sys.stdin = open('input/미로_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sc, sr = 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                gc, gr = c, r
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    stack = []
    n = len(stack)
    while True:
        if n == 0:
            pass
        for i in range(4):
            dr, dc = gr + dy[i], gc + dx[i]
            if arr[dr][dc] == 0:
                point = [dr, dc]
                stack.append(point)
    print(stack)