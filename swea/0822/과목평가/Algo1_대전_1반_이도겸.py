# import sys; sys.stdin = open('input/algo1_sample_in.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    sr, sc, er, ec = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_v = 0  # 평탄화 작업할 땅의 합
    nzero = 0   # 편탄화 작업할 땅의 영역

    # 평탄화 작업할 영역의 기준 정하기
    for r in range(sr, er + 1):         # 세로의 시작점부터 끝지점까지
        for c in range(sc, ec + 1):     # 가로의 시작점부터 끝지점까지
            sum_v += arr[r][c]          # 영역의 합
            nzero += 1                  # 영역의 크기
    base = sum_v//nzero                 # 평탄화 작업기준

    cnt = 0     # 작업량 카운트
    # 평탄화 작업 시작
    for r in range(sr, er + 1):         # 세로의 시작점부터 끝지점까지
        for c in range(sc, ec + 1):     # 가로의 시작점부터 끝지점까지
            b = arr[r][c] - base        # 현재 땅과 평균 사이의 차이
            if b == 0:  # 차이가 0이면 pass
                pass
            elif b != 0:
                if b < 0:       # 차이가 음수이기 때문에 차이를 빼주고 카운트에서도 빼줘야한다.
                    arr[r][c] -= b
                    cnt -= b
                elif b > 0:     # 차이가 양수이면 평탄화 작업을 위해 빼주고 카운트를 더해준다.
                    arr[r][c] -= b
                    cnt += b

    print(f'#{tc} {cnt}')