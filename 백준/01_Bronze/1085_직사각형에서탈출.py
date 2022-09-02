x, y, w, h = map(int, input().split())

# min_v = 9999999999999999999999
# if min_v > w-x:
#     min_v = w-x
# if min_v > x:
#     min_v = x
# if min_v > h-y:
#     min_v = h-y
# if min_v > y:
#     min_v
# print(min_v)

a = [w-x, x, h-y, y]
print(min(a))