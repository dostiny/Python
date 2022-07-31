students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

students_dict = {}

for people in students:
    if people in students_dict:
        students_dict[people] += 1
    else:
        students_dict[people] = 1

students_dict = sorted(students_dict.items(), key=lambda x:x[1], reverse=True)
leader =  students_dict[0]
print(f'우리반 반장은 {leader[1]}표를 받은 {leader[0]}가 반장입니다.')