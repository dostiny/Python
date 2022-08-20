import sys; sys.stdin = open('input/5356_input.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [[] for _ in range(5)]
    arr = [list(input()) for _ in range(5)]

    for i in range(5):
        N = 15 - len(arr[i])
        arr[i] += [''] * N

    str = ''
    for r in range(15):
        for c in range(5):
            if arr[c][r] != '':
                str += arr[c][r]
            else:
                pass
    print(f'#{tc} {str}')