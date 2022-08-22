arr = [64, 25, 10, 22, 11]
N = len(arr)

for j in range(N - 1):
    min_idx = j
for i in range(j+1, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
arr[min_idx], arr[0] = arr[0], arr[min_idx]

# min_idx = 0
# for i in range(1, N):
#     if arr[min_idx] > arr[i]:
#         min_idx = i
# arr[min_idx], arr[0] = arr[0], arr[min_idx]
#
# min_idx = 1
# for i in range(1, N):
#     if arr[min_idx] > arr[i]:
#         min_idx = i
# arr[min_idx], arr[1] = arr[1], arr[min_idx]
#
# min_idx = 2
# for i in range(3, N):
#     if arr[min_idx] >arr[i]
#         miv_idx = i
# arr[min_idx], arr[2] = arr[2]

print(arr)