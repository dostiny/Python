blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_dict = {}

for people in blood_types:
    if people in blood_dict:
        blood_dict[people] += 1
    else:
        blood_dict[people] = 1

print(blood_dict)