input_word = input()
howlong = len(input_word)

if howlong % 2:
    print(input_word[howlong//2])
else:
    print(input_word[howlong//2-1:howlong//2+1])