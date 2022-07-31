words = ''
word = []

while words != 'done':
    words = input()
    word.append(words)
    a = 0
    if a == 0:
        a += 1
    elif a > 0 and word[a-1][-1] != word[a][0]:
        print('탈락')
        a += 1

print(word)