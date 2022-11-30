import sys

sys.stdin = open('input/12386_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [int(i) for i in input()]
    big_v = 0
    max_cnt = 0
    for j in arr:
        cnt = 0
        for k in arr:
            if j == k:
                cnt += 1
        if cnt == 1 or cnt == 0:
            if big_v < j:
                big_v = j
                max_cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
            big_v = j
    print(f'#{test_case} {big_v} {max_cnt}')
