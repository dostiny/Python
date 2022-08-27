nan = [int(input()) for _ in range(9)]
n = len(nan)
for i in nan:
    for j in nan:
        if i != j:
            sum_v = sum(nan) - i - j
            if sum_v == 100:
                a, b = i, j
ans = []
for k in nan:
    if k == a or k == b:
        pass
    else:
        ans.append(k)
        ans.sort()
for an in ans:
    print(an)