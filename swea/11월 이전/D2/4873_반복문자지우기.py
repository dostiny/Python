import sys; sys.stdin = open('input/12399_input.txt', 'r')

for tc in range(1, int(input())+1):
    st = input()
    N = len(st)
    st_li = [0] * N
    top = -1
    for i in st:
        top += 1
        st_li[top] = i
        if top == 0:    # top 가 0 일때는 그냥 지나가도록 조건 추가
            pass
        elif st_li[top-1] == st_li[top]:
            top -= 2
    print(f'#{tc} {top+1}')