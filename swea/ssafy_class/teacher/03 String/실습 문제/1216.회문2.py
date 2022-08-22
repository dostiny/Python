import sys; sys.stdin = open('1216.txt')

# 교수님 풀이로 제출 후 추가로 다시 제출 예정
def find_palindrome(arr, N, M):
    # 모든 행에 대해서
    # 모든 가능한 경우/ 회문이 있을 수 있는 시작 위치
    for row in range(N):
        for s in range(N - M + 1):
            e = s + M - 1
            for i in range(M//2):
                if arr[row][s + i] != arr[row][e - i]:
                    break
            else:
                return M

        for s in range(N - M + 1):
            e = s + M - 1
            for i in range(M//2):
                if arr[s + i][row] != arr[e - i][row]:
                    break
            else:
                return M
    return 0

for tc in range(1, 11):
    tc_num = input()
    arr = [input() for _ in range(100)]

    ans = 0
    for M in range(100, 1, -1):  # 100 ~ 2
        ans = find_palindrome(arr, 100, M)
        if ans != 0:
            break
    print(f'#{tc} {ans}')