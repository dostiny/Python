import sys; sys.stdin = open('input/algo2_sample_in.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())        # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]       # 배열 입력
    patten = [list(map(int, input().split())) for _ in range(3)]    # 패턴 입력
    cnt = 0

    for r in range(N+1-3):          # 세로 방향 시작점 범위
        for c in range(N+1-3):      # 가로 방향 시작점 범위
            f_arr = [[0] * 3 for _ in range(3)]     # 패턴 비교를 위한 빈 리스트 초기화
            for y in range(3):      # 패턴의 세로 범위
                for x in range(3):  # 패턴의 가로 범위
                    if arr[r+y][c+x] == 1:  # 시작점 범위 + 패턴의 범위를 비교 했을때 1인 상황
                        f_arr[y][x] = 1     # 1일때 빈 리스트 위치에 1 입력
            if patten == f_arr:     # 패턴 비교
                cnt += 1
    print(f'#{tc} {cnt}')
