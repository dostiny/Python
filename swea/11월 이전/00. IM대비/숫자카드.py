import sys; sys.stdin = open('input/12386_input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input()))
    result = 0
    num = 0
    for i in range(N):
        cnt = 0
        for j in arr:
            if arr[i] == j:
               cnt += 1
        if result < cnt:
            num = arr[i]
            result = cnt
    if result == 1:
        for n in arr:
            if num < n:
                num = n
    print(f'#{tc}', num, result)