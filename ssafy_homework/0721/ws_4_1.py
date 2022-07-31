pwd = ''
count = 1

while pwd != '1234' and count <= 3:
    pwd = input('비밀번호 입력하세요 : ')
    count += 1

if count > 3:
    print('비밀번호 입력 오류가 3번 발생하여, 처리 불가')
else:
    print('비밀번호가 정확합니다')