import sys; sys.stdin = open('오목_input.txt')

dy = [0, 1, 1, 1]  # 우 우하 하 좌하
dx = [1, 1, 0, -1]  # 우 우하 하 좌하

def five():
    for r in range(N):
        for c in range(N):
            if bing[r][c] == '.':
                continue
            for d in range(4):
                for i in range(5):
                    dr = r + dy[d] * i
                    dc = c + dx[d] * i
                    if 0 > dr or dr >= N or 0 > dc or dc >= N or bing[dr][dc] == '.':
                        break
                else:
                    return 'YES'
    return 'NO'

for test_case in range(1, int(input())+1):
    N = int(input())
    bing = [list(map(str, input())) for _ in range(N)]
    print(f'#{test_case} {five()}')