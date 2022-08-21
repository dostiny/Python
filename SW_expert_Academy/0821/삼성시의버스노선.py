import sys; sys.stdin = open('input/s_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0 for _ in range(5001)]
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            arr[i] += 1
    print(f'#{tc}', end=' ')
    for _ in range(int(input())):
        c = int(input())
        print(arr[c], end=' ')
    print()