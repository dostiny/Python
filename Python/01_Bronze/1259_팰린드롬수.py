while True:
    N = input()
    result = 1
    if int(N) == 0:
        break
    n = len(N)//2
    for i in range(n):
        if N[i] != N[-(i+1)]:
            result = 0
            break
    if result == 0:
        print('no')
    else:
        print('yes')