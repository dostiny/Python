# input() ==> 문자열
# input().split() ==> 문자열리스트
# map(int, input().split()) ==> 정수들의 리스트
import sys; sys.stdin = open('test.txt', 'r')

for tc in range(10):
    # 하나의 테스트 케이스
    N = int(input())    #자료수
    arr = list(map(int, input().split()))

    # 나의 아이디어를 코딩
    print(f'#{tc} {N}')