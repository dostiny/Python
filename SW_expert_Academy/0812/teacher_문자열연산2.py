# strlen() 함수 구현해보기
mystr = 'algorithm'
# # 1. 파이썬의 내장된 기능
# print(mystr[::-1])
#
# # 2. 새로운 공간에 저장
# rev_str  = ''
# for i in range(len(mystr) -1, -1, -1):
#     rev_str += mystr[i]
# print(rev_str)

# 3. 교환을 통해서 뒤집기
arr = list(mystr)
# 3-1. 내 풀이
for i in range(len(arr)//2):
    arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
print(''.join(arr))
# 3-2. 교수님
N = len(arr) # len값을 변수에 추가해주면 편함
for i in range(N//2):
    arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
print(''.join(arr))