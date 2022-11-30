import sys; sys.stdin = open('input/12394_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    str_li = [list(input()) for _ in range(N)]
    str = ''
    for st in str_li:
        for i in st:
            pass
