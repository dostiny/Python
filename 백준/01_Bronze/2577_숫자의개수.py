num = [int(input()) for _ in range(3)]
val = 1
for i in num:
    val *= i
val = str(val)
v_li = list(map(int, val))
arr = [0] * 10
