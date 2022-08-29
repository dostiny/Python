arr = [int(input()) for _ in range(3)]
val = 1
for i in arr:
    val *= i
val = str(val)
v_li = list(map(int, val))
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num:
    cnt = 0
    for j in v_li:
        if i == j:
            cnt += 1
    print(cnt)