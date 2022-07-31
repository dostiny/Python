s = input('숫자를 입력해주세요 : ')
s_num = int(s)
num = 0

while s_num > 10:
    num += s_num%10
    s_num = s_num // 10
num += s_num

print(num)