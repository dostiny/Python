for tc in range(1, int(input())+1):
    arr = list(input().split())
    new_arr = []
    for i in arr:
        if i == '.':
            if len(new_arr) == 1:
                result = new_arr[0]
            else:
                result = 'error'
        elif i == '+' or i == '-' or i == '*' or i == '/':
            if len(new_arr) > 1:
                if i == '+':
                    num2 = new_arr.pop()
                    num1 = new_arr.pop()
                    new_num = int(num1) + int(num2)
                    new_arr.append(new_num)
                elif i == '*':
                    num2 = new_arr.pop()
                    num1 = new_arr.pop()
                    new_num = int(num1) * int(num2)
                    new_arr.append(new_num)
                elif i == '-':
                    num2 = new_arr.pop()
                    num1 = new_arr.pop()
                    new_num = int(num1) - int(num2)
                    new_arr.append(new_num)
                elif i == '/':
                    num2 = new_arr.pop()
                    num1 = new_arr.pop()
                    new_num = int(num1) // int(num2)
                    new_arr.append(new_num)
            else:
                result = 'error'
                break
        else:
            new_arr.append(i)

    print(f'#{tc} {result}')