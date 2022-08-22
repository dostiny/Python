import sys; sys.stdin = open('input/10804_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    mystr = input()
    arr = list(mystr)
    N = len(arr)
    rearr = []
    for i in range(N//2):
        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
    for j in arr:
        if j == 'b':
            rearr += 'd'
        elif j == 'p':
            rearr += 'q'
        elif j == 'd':
            rearr += 'b'
        elif j == 'q':
            rearr += 'p'
    print(f'#{test_case}', end=' ')
    print(''.join(rearr))