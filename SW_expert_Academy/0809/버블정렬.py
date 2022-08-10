arr = [55, 7, 78, 12, 42]
N = len(arr)

# for i in range(0, N-2 + 1):
#     for j in range(0, N-2 + 1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
# print(arr)

# for i in range(0, N-2 + 1):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
# print(arr)
#
# for i in range(0, N-3 + 1):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
# print(arr)

for i in range(N - 1, 0, -1):   # n-1 부터 1 까지
    for j in range(0, i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)