import sys; sys.stdin = open('input/12397_input.txt', 'r')

def function(N):
    if N%10 == 0:
        if N == 10:
            return 1
        elif N == 20:
            return 3
        else:
            return function(N-10) + (2 * function(N-20))

for tc in range(1, int(input())+1):
    N = int(input())
    print(f'#{tc} {function(N)}')