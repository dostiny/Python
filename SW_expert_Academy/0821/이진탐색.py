for tc in range(1, int(input())+1):
    P, a, b = map(int, input().split())
    ai, ar = 1, P
    bi, br = 1, P
    ac, bc = 0, 0
    while True:
        ac, bc = int((ai + ar) / 2), int((bi + br) / 2)

        if ac == a and bc == b:
            print(f'#{tc} {0}')
            break
        elif ac == a:
            print(f'#{tc} A')
            break
        elif bc == b:
            print(f'#{tc} B')
            break

        if a < ac:
            ar = ac
        elif a > ac:
            ai = ac

        if b < bc:
            br = bc
        elif b > bc:
            bi = bc