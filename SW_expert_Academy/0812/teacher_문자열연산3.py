# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
#
# print(f's1:{s1},s2:{s2},s3:{s3},s4:{s4},s5:{s5}')
# print('=======================')
# print('s1 / s2 :', s1 == s2, s1 is s2)
# print('s1 / s3 :', s1 == s3, s1 is s3)
# print('s1 / s4 :', s1 == s4, s1 is s4)
# print('s1 / s5 :', s1 == s5, s1 is s5)

def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x)-ord('0')
    return i

s = '123'
a = atoi(s)
print(a)
print(a + 1)