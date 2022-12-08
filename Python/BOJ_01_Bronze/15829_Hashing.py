N = int(input())
strli = list(input())
result = 0

for i in range(N):
    result += (ord(strli[i]) - 96) * (31 ** i)
print(result % 1234567891)