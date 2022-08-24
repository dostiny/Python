# 양의 정수를 입력받아 문자열로 변환하는 함수

def itoa(num):
    arr = []
    while num != 0:
        arr += chr(num%10+48)
        num = num//10
    N = len(arr)
    for i in range(N//2):
        arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
    strnum = ''.join(arr)
    return strnum
val = itoa(1234)
print(type(val), val)