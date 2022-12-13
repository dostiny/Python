import sys
arr = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
for _ in range(int(sys.stdin.readline())):
    stli = sys.stdin.readline().strip().split()
    if len(stli) == 2:
        st, num = stli
        num = int(num)
    else:
        st = stli[0]
    if st == 'add' and arr[num] == 0:
        arr[num] = 1
    elif st == 'remove' and arr[num]:
        arr[num] = 0
    elif st == 'check':
        if arr[num] == 1:
            print(1)
        else:
            print(0)
    elif st == 'toggle':
        if arr[num] == 0:
            arr[num] = 1
        else:
            arr[num] = 0
    elif st == 'all':
        for i in range(1, 21):
            arr[i] = 1
    elif st == 'empty':
        for i in range(1, 21):
            arr[i] = 0
    # print(f'{st}, {num}')
    # print(arr)


# # =====================================
# S = set()
# for _ in range(int(input())):
#     stli = input().split()
#     if len(stli) == 2:
#         st, num = stli
#         num = int(num)
#     else:
#         st = stli[0]
#     if st == 'add':
#         S.add(num)
#     elif st == 'remove':
#         S.discard(num)
#     elif st == 'check':
#         print(1 if num in S else 0)
#     elif st == 'toggle':
#         if num in S:
#             S.discard(num)
#         else:
#             S.add(num)
#     elif st == 'all':
#         S = set([i for i in range(1, 21)])
#     elif st == 'empty':
#         S = set()