while True:
    arr = list(map(int, input().split()))
    arr.sort()
    a, b, c = arr[0], arr[1], arr[2]
    if a == 0 and b == 0 and c == 0:
        break
    elif c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')