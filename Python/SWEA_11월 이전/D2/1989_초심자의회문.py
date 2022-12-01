import sys; sys.stdin = open('input/1989_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    mystr = input()
    N = len(mystr)
    TorF = 0
    for i in range(N//2):
        if mystr[i] == mystr[N-1-i]:
            TorF = 1
        else:
            TorF = 0
    print(f'#{test_case} {TorF}')