for _ in range(int(input())):
    arr = list(input())
    c = len(arr)//2
    list1 = arr[:c]
    list2 = arr[c + 1:]
    print('Possible' if sorted(list1) == sorted(list2) else 'Impossible')