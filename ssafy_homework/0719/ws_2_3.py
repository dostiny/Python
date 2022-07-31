# saFe eMotion Nail

word = input().lower().split()

if word[0][-1] == word[1][0]:
    if word[1][-1] == word[2][0]:
        print('pass')
    else :
        print('Fall')
else :
    print('Fail')