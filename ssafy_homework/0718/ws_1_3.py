security_number = input('주빈번호를 입력하세요 : ')

front_number = security_number[:6]
back_number = '*'*7

print(front_number+back_number)