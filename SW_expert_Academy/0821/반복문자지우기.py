import sys; sys.stdin = open('input/반복문자지우기_input.txt', 'r')

for tc in range(1, int(input())+1):
    st = input()
    N = len(st)
    st_li = [0 for _ in range(N)]
    top = -1
    for i in st:
        top += 1
        st_li[top] = i
        if st_li[top-1] == st_li[top]:
            top -= 2
    print(f'#{tc} {top+1}')