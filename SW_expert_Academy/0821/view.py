import sys; sys.stdin = open('input/1206_input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        max_v = 0
        a, b, c, d, e = arr[i-2], arr[i-1], arr[i], arr[i+1], arr[i+2]
        if c < a or c < b or c < d or c < e:
            continue
        else:
            bild = [a, b, d, e]
            for i in bild:
                if max_v < i:
                    max_v = i
            cnt += c - max_v

    print(f'#{tc} {cnt}')