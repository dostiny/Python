data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

size = len(data) + 1
H = [0] * size
last = 0

def push(item):
    global last
    last += 1
    H[last] = item
    p, c = last // 2, last

    # 자식이 부모보다 작으면 스위칭
    while p > 0 and H[c] < H[p]:
        H[c], H[p] = H[p], H[c]
        c = p
        p = c // 2

for val in data:
    push(val)

for i in range(1, size):
    print(H[i])
