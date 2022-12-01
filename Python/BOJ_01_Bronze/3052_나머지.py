arr = [int(input()) for _ in range(10)]

div_arr = []
for i in arr:
    num = i % 42
    div_arr.append(num)
num_set = set(div_arr)
n = len(num_set)
print(n)