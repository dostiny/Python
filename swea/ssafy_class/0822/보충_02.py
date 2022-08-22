# 순열 - 금은동 메달

# arr = ['A', 'B', 'C', 'D']
# path = [''] * 3
# used = [0] * 4
# def abc(level):
#     if level == 3:
#         for i in range(3):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(4):
#         if used[i] == 1: continue
#         used[i] = 1
#         path[level] = arr[i]
#         abc(level + 1)
#         used[i] = 0
#
# abc(0)



# 조합 - 팀 만들기

# arr = ['A', 'B', 'C', 'D']
# path = [''] * 3
# def abc(level):
#     if level == 3:
#         for i in range(3):
#             print(path[i], end=' ')
#         print()
#         return
#
#     for i in range(4):
#         if level > 0 and path[level-1] >= arr[i]: continue
#         path[level] = arr[i]
#         abc(level + 1)
#
# abc(0)


# ver2
arr = ['A', 'B', 'C', 'D']
path = [''] * 3
def abc(level, start):
    if level == 3:
        for i in range(3):
            print(path[i], end=' ')
        print()
        return

    for i in range(start, 4):
        if level > 0 and path[level-1] >= arr[i]: continue
        path[level] = arr[i]
        abc(level + 1, i+1)

abc(0, 0)   # level