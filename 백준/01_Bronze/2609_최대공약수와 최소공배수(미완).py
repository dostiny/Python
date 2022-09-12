num1, num2 = map(int, input().split())

a = b = c = d = e = f = g = 0
if num1 % 2 == 0 and num2 % 2 == 0:
    num1, num2 = num1 // 2, num2 // 2
    a += 1
elif num1 % 3 == 0 and num2 % 3 == 0:
    b += 1
elif num1 % 5 == 0 and num2 % 5 == 0:
    c += 1
elif num1 % 7 == 0 and num2 % 7 == 0:
    d += 1
elif num1 % 11 == 0 and num2 % 11 == 0:
    e += 1
elif num1 % 13 == 0 and num2 % 13 == 0:
    f += 1
elif num1 % 17 == 0 and num2 % 17 == 0:
    g += 1

