# 저장공간 생성
S = [0] * 10
top = -1

def push(item):
    global top
    # full 상태를 체크 top이 배열의 마지막 인덱스인지 아닌지
    top += 1
    S[top] = item

def pop():
    global top
    # empty 상태를 체크, top이 -1인지
    val = S[top]
    top -= 1
    return val