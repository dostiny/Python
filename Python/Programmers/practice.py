def solution(quiz):
    answer = []
    for li in quiz:
        arr = list(li.split())
        print(arr)
        for i in arr:
            print(i)
            if i == ' ':
                pass
            elif i == '-':
                pass
            elif i == '+':
                pass
            elif int(i):
                print(i)
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))