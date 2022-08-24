# n개의 주사위 모든 경우의 수
# n = int(input())
#
# def sq(n):
#     if n == 0:
#         return
#
#     for i in range(1, 7):
#         print(i, end=' ')
#     print()
#
# sq(4)

# A B C D 가 적힌 카드가 있습니다.
# A B C D 가 적힌 카드 묶음이 3 묶음 있습니다.
# 각 묶음 에서 카드를 1장씩 뽑았을때 나올수 있는 모든 경우를 다 출력
# lever 3, br 4
arr = ['A', 'B', 'C', 'D']
path = ['']*3

def abc(level):
    if level == 3:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return

    for i in range(4):
        path[level] = arr[i]
        abc(level + 1)

abc(0)