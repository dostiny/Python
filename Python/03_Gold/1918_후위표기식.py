arr = list(input())
stack = []
result = ''

for i in arr:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':              # 먼저 들어오고 같은 우선순위에 있는 *,/는 result에 넣어줌
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':              # +, - 보다 낮은 우선 순위가 없어서 연산자면 전부 result에 넣어줌
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':                          # 닫음 괄호와 열음 괄호 사이에 있는 연산자들 전부 반환
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()
print(result)