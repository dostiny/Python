words_dict = {'proper' : '적절한',
              'possible' : '가능한',
              'moral' : '도덕적인',
              'patient' : '참을성 있는',
              'balance' : '균형',
              'perfect' : '완벽한',
              'logical' : '논리적인',
              'legal' : '합법적인',
              'relevant' : '관련 있는',
              'responsible' : '책임감 있는',
              'regular' : '규칙적인'}

words_dict2 = {}

for key, value in words_dict.items():
    if key[0] == 'b':
        words_dict2['im' + key[1:]] = value
    elif key[0] == 'm':
        words_dict2['im' + key[1:]] = value
    elif key[0] == 'p':
        words_dict2['im' + key[1:]] = value
    elif key[0] == 'l':
        words_dict2['il' + key[1:]] = value
    elif key[0] == 'r':
        words_dict2['ir' + key[1:]] = value

print(words_dict2)