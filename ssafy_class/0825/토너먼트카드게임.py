import sys; sys.stdin = open('input/토너먼트카드게임_input.txt', 'r')

# 1: 가위, 2: 바위, 3: 보
#          1  2  3
lose = [0, 2, 3, 1]
def play(s, e):
    if s == e:
        return s
    else:
        mid = (s + e) // 2
        lwin = play(s, mid)
        rwin = play(mid + 1, e)

        if lose[arr[lwin]] == arr[rwin]:
            return rwin
        return lwin

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = play(0, len(arr) - 1)
    print(ans + 1)
