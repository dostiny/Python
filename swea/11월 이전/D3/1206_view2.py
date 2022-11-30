import sys

sys.stdin = open('input/1206_view_input.txt', 'r')

# T = int(input())
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))   # 1차원 배열을 입력받는 방법

    result = 0  # 조망권 확보 세대수
    for i in range(2, N-2):
        max_value = 0   # i-2, i-1, i+1, i+2 중에 최대값
        for j in range(5):
            if j != 2:
                if max_value < arr[i-2+j]:
                    max_value = arr[i-2+j]
        # i 좌우 2개의 최대값이 i의값 보다 작으면 조망권 확보
        if arr[i] > max_value:
            result += arr[i] - max_value
    print(f'#{test_case} {result}')