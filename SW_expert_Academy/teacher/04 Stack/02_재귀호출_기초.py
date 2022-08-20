#=======================================
i = 0
while i < 3:
    print('Hello') # 반복할 작업
    i += 1

# 재귀 호출(1)
def print_hello(i):
    if i == 3:
        return
    else:
        print('Hello')  # 반복할 작업
        print_hello(i + 1)
print_hello(0)
#=======================================
def print_hello(i):
    if i == 3:
        return
    else:
        print('Hello', i)  # 반복할 작업
        print_hello(i + 1)
        print('Bye', i)  # 반복할 작업
print_hello(0)
# ==============================
cnt = 0
def print_hello(i):
    if i == 3:
        global cnt
        cnt += 1
    else:
        print_hello(i + 1)
        print_hello(i + 1)

print_hello(0)
print('cnt= ', cnt)

# ==============================
# 최소 값 찾기
arr = [55, 17, 33, 26, 66, 78, 42, 42]

def find_min(s, e):
    if s == e:
        return arr[s]
    else: # s < e
        mid = (s + e) // 2
        l = find_min(s, mid)
        r = find_min(mid + 1, e)
        return l if l < r else r

print(find_min(0, len(arr) - 1))