import sys
sys.stdin = open('12391_input.txt', 'r')

for test_case in range(1, int(input())+1):
    P, A, B = map(int, input().split())
    al, ar = 1, P
    bl, br = 1, P
    ac, bc = 0, 0
    while True:
        ac = int((al + ar) / 2)
        bc = int((bl + br) / 2)
        if ac == A and bc == B:
            print(f'#{test_case} {0}')
            break
        elif ac == A:
            print(f'#{test_case} A')
            break
        elif bc == B:
            print(f'#{test_case} B')
            break

        if A > ac:
            al = ac
        elif A < ac:
            ar = ac

        if B > bc:
            bl = bc
        elif B < bc:
            br = bc

