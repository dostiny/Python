for TC in range(1, int(input()) + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        inli = list(input().split())
        for _ in range(int(inli[1])):
            arr.append(inli[0])
    print(f'#{TC}')
    for i in range(len(arr)):
        if i%10 == 0 and i != 0:
            print()
        print(arr[i], end='')
    print()