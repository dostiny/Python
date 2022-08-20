import sys

sys.stdin = open('input/1206_view_input.txt', 'r')

# T = int(input())
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))   # 1차원 배열을 입력받는 방법
    print(arr)

    total_num = 0
    for i in range(2, len(arr)-1):
        i_arr = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        i_num = 0
        for j in i_arr:
            if i_num < j:
                i_num = j
        if i > i_num:
            total_num += (i - i_num)
    print(total_num)