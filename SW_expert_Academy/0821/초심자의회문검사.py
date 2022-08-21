for tc in range(1, int(input())+1):
    st = input()
    N = len(st)
    n = N//2
    for i in range(n):
        if st[i] == st[N-1-i]:
            result = 1
        else:
            result = 0
    print(f'#{tc} {result}')