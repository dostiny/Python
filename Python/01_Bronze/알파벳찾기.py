s = list(map(str, input()))
n = len(s)
ans = [-1] * 26
alpa = []
for i in range(97, 123):
    alpa.append(chr(i))
for j in range(26):
    for k in range(n):
        if alpa[j] == s[k]:
            if ans[j] == -1:
                ans[j] = k
print(*ans)