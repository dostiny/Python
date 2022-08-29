T, M = map(int, input().split())
t, m = 0, 0
if M - 45 < 0:
    m = M - 45 + 60
    if T == 0:
        t = 23
    else:
        t = T - 1
else:
    m = M - 45
    t = T

print(t, m)