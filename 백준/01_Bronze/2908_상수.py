num1, num2 = map(str, input().split())

num1i = []
num2i = []
for i in range(3):
    num1i.append(int(num1[i]))
    num2i.append(int(num2[i]))
numv1 = num1i[2] * 100 + num1i[1] * 10 + num1i[0]
numv2 = num2i[2] * 100 + num2i[1] * 10 + num2i[0]

if numv1 < numv2:
    print(numv2)
else:
    print(numv1)