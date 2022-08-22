# 숫자카드 확인용
import sys
sys.stdin = open('12386_input.txt', 'r')

for tc in range(1, int(input()+1)):
    N = int(input())
    nums = list(map(int, input()))

    # 카운팅 배열 생성
    # 자료의 범위가 0에서 9까지
    cnt = [0] * 10
    for num in nums:
        cnt[num] += 1
        # cnt의 최대값의 인덱스 찾기
        max_idx = 0
        for i in range(1, 10):
            if cnt[max_idx] <= cnt[i]:
                max_idx = i
        print(max_idx, cnt[max_idx])