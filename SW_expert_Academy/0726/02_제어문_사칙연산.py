num = num = int(input())

for i in range(1, num+1):
    num_list = list(map(str, input().split()))
    if num_list[-1] == '+':
        numbers = int(num_list[0]) + int(num_list[1])
    elif num_list[-1] == '-':
        numbers = int(num_list[0]) - int(num_list[1])
    elif num_list[-1] == '*':
        numbers = int(num_list[0]) * int(num_list[1])
    elif num_list[-1] == '/':
        numbers = int(int(num_list[0]) / int(num_list[1]))
    elif num_list[-1] == '//':
        numbers = int(num_list[0]) // int(num_list[1])
    elif num_list[-1] == '%':
        numbers = int(num_list[0]) % int(num_list[1])
    print(f'#{i} {numbers}')