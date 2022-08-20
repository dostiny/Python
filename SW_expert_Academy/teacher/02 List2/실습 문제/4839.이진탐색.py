import sys; sys.stdin = open("4839.txt", "r")


# 이진 탐색

# 찾을 범위에서 중간 위치의 값을 선택
def binary_search(N, key):
    start, end = 1, N
    cnt = 0
    while start <= end: # start == end 이면 mid == start == end 가 된다.
        mid = (start + end) // 2
        cnt += 1
        if key == mid: # 찾음!!!
            return cnt
        elif key < mid: # 왼쪽에서 찾아야지
            end = mid - 1
        else:
            start = mid + 1
    return 0

for tc in range(1, int(input()) + 1):
    P, A, B = map(int, input().split())

    cntA = binary_search(P, A)
    cntB = binary_search(P, B)

    print(cntA, cntB)