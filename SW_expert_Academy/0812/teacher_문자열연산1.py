# strlen() 함수 구현해보기

# 내 풀이
# def strlen(arr):
#     i = 0
#     while True:
#         if arr[i] == '\0':
#             return i
#         else:
#             i += 1

# 나이스한풀이
def strlen(arr):
    i = 0
    while arr[i] != '\0':
        i += 1
    return i
# while 문으로 작성

arr = ['s', 's', 'a', 'f', 'y', '\0']

print(strlen(arr))


