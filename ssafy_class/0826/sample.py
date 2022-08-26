import sys; sys.stdin = open('input/tree_input.txt', 'r')

V, E = map(int,input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1)   # 1번 ~ V번 까지의 노드번호 사용
R = [0] * (V + 1)   #
P = [0] * (V + 1)

for i in range(0, E*2, 2):
    parent, child = arr[i], arr[i + 1]
    if L[parent] == 0:
        L[parent] = child
    else:
        R[parent] = child
    P[child] = parent

def inorder(v):
    if v == 0:
        return
    # 전위 순회
    inorder(L[v])
    # 중위 순회
    print(v, end=' ')
    inorder(R[v])
    # 후위순회
inorder(1)




'''
전위 중위 후위 고정
def inorder(v):
    inorder(L[v])

    inorder(R[v])
'''