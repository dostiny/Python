for tc in range(1, int(input())+1):
    st = list(map(str, input()))
    N = len(st)
    n = N//2
    for s in range(n):
        st[s], st[N-1-s] = st[N-1-s], st[s]

    for s in range(N):
        if st[s] == 'q':
            st[s] = 'p'
        elif st[s] == 'p':
            st[s] = 'q'
        elif st[s] == 'b':
            st[s] = 'd'
        elif st[s] == 'd':
            st[s] = 'b'

    print(f'#{tc}', end=' ')
    for i in st:
        print(i, end='')
    print()
