data = [50, 30, 24, 5, 28, 45, 98, 52, 60]
# while True:
#     try:
#         data.append(int(input()))
#     except:
#         break
# print(data)

def treee(idx):
    global node
    if len(data) < idx:
        return

    if idx == 0 and node == 1:
        T[node] = data[idx]
        idx += 1
    else:
        if T[node] > data[idx]:
            node = node * 2
            T[node] = data[idx]
        else:
            if T[node] < data[idx]:
                pass
    treee(idx)

size = len(data) * 3
T = [0] * size
L = [0] * size
R = [0] * size
node = 1
idx = 0
print(len(data))