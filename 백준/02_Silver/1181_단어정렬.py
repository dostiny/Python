N = int(input())
arr = list(set([input() for i in range(N)]))
s = [0] * 51
for i in arr:
    n = len(i)
    if s[n] == 0:
        s[n] = [i]
    else:
        s[n] += [i]
for j in s:
    if j != 0:
        j.sort()
        for k in j:
            print(k)