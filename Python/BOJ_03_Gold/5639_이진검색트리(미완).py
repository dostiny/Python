
# while True:
#     try:
#         data.append(int(input()))
#     except:
#         break
# print(data)



def treee(k, node):
    if k == n:
        return
    else:
        for i in data:
            if T[node] == 0:
                T[node] = i
            else:
                if T[node] > i:
                    nod = node * 2
                    T[nod] = i
                    k += 1
                elif T[node] < i < T[node//2]:
                    nod = node * 2 + 1
                    T[nod] = i
                    k += 1
                elif T[node] < i:
                    nod = node // 2
                treee(k, nod)

data = [50, 30, 24, 5, 28, 45, 98, 52, 60]
n = len(data)
size = n * 3
T = [0] * size
L = [0] * size
R = [0] * size
node = 1
idx = 0
print(len(data))