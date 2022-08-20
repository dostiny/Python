import sys; sys.stdin = open('input/12394_input.txt', 'r')


# 행(문자열)에서 주어진 길이의 회문을 찾을 수 있으면 ok
arr = 'JHYXHBQTLMMHOOOHMMLT'
N = 20
M = 13
# 모든 가능한 경우 / 회문이 있을 수 있는 시작 위치
for s in range(N - M + 1):
    e = s + M - 1
    for i in range(M//2):
        if arr[s + i] != arr[e - i]:
            break
    else:
        ans = ''
        for i in range(s, e + 1):
            ans += arr[i]
        break
print(ans)