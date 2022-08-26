import sys; sys.stdin = open('input/IM_Magnetic_input.txt', 'r')
'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for c in range(N):
        nc, sc, ns_li = 0, 0, []
        for r in range(N):
            if arr[r][c] == 1:
                nc += 1
                ns_li.append(arr[r][c])
            elif arr[r][c] == 2:
                sc += 1
                ns_li.append(arr[r][c])

        if nc == 0 or sc == 0:
            for r in range(N):
                arr[r][c] = 0
        else:
            for ma in ns_li:
                pass