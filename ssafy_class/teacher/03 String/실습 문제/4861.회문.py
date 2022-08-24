import sys; sys.stdin = open('4861.txt', 'r')

# 행(문자열)에서 주어진 길이의 회문을 찾을 수 있으면 OK!!!
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
                ans = ''
                for i in range(s, e + 1):
                    ans += arr[row][i]
                return ans

        for s in range(N - M + 1):
            e = s + M - 1
            for i in range(M//2):
                if arr[s + i][row] != arr[e - i][row]:
                    break
            else:
                ans = ''
                for i in range(s, e + 1):
                    ans += arr[i][row]
                return ans

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ret = find_palindrome(arr, N, M)
    print(ret)
