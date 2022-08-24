import sys; sys.stdin = open('input/암호_input.txt', 'r')

QSIZE = 9
Q = [0] * QSIZE
fornt = rear = 0

def enquene(item):
    pass

def dequeue():
    pass

def isFull():
    pass

def isEmpty():
    pass

tc_num = input()
arr = list(map(int, input().split()))

for val in arr:
    enqueue(val)

cnt = 1
while Q[rear]:
    val = dequeue()
    val -= cnt
    cnt = 1 if cnt == 5 else cnt + 1
    val = 0 if val < 0 else val
    enqueue(val)

print(Q)