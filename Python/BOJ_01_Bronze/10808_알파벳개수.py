st = list(input())
alpa = [0] * 26

for i in st:
    alpa[ord(i)-97] += 1
for j in alpa:
    print(j, end=' ')
print()