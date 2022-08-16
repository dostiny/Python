numli = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(numli)
arr = list(map(int, input().split()))
asc = 0
des = 0
for i in range(n):
    if numli[i] == arr[i]:
        asc += 1
    elif numli[0-i-1] == arr[i]:
        des += 1
if asc == 8:
    print('ascending')
elif des == 8:
    print('descending')
else:
    print('mixed')