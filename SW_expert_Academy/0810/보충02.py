import sys
sys.stdin = open('input/보충02_input.txt', 'r')

for test_case in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 초기 maxsum값 지정
    Max = 0
    for i in range(100):
        Max += arr[0][i] # 첫번째 행의 합 구하기

    # 1 가로 합 구하기 그리고 MAx값 갱신
    for i in range(1, 100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum > Max:
            Max = sum

    # 2 세로 합 구하기 그리고 MAx값 갱신
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if Max < sum:
            Max = sum

    # 3 대각선1 합 구하기 그리고 MAx값 갱신
    sum = 0
    for i in range(0, 100):
        sum += arr[i][i]
    if Max < sum:
        Max = sum

    # 4 대각선2 합 구하기 그리고 Max값 갱신
    sum = 0
    for i in range(0, 100):
        sum += arr[i][99 - i]
    if Max < sum:
        Max = sum

    print(f'#{test_case + 1} {Max}')