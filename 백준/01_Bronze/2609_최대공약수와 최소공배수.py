num1, num2 = list(map(int, input().split()))
num3, num4 = num1, num2
while num2 != 0:
    num1, num2 = num2, num1 % num2
print(num1)
result = (num3 * num4) // num1
print(result)