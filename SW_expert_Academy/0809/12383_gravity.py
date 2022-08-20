import sys

sys.stdin = open('input/12383_gravity_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(N):
        # 상자에서 벽까지 거리
        height = N - 1 - i
        # 및에 깔리는 상자들의 개수 카운팅
        for j in range(i + 1, N):
            if arr[i] <= arr[j]:
                height -= 1

        if result < height:
            result = height

    print(f'#{test_case} {result}')
