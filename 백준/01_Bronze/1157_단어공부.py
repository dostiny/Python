alpa = list(map(str, input().upper()))
alpa_set = set(alpa)
max_v = 0
cnt = 0
ans = 0
for i in alpa_set:
    cnt = alpa.count(i)
    if max_v < cnt:
        max_v = cnt
        ans = i
    elif max_v == cnt:
        ans = '?'
print(ans)