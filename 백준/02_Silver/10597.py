def back(n):
    global num
    for i in arr:
        if int(i) in result:
            if num == 0:
                num = i
            else:
                pass


arr = list(input())
num = 0
result = []
back()
print(arr)