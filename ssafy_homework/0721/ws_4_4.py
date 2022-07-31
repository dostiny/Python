str_input = input()
str_list = str_input.split()
word_list = []
num = 0

for word in str_list:
    for i in word:
        num += ord(i)
    word_list.append(num)
    num = 0
    
num2 = 0
for j in range(len(word_list)):
    if word_list[j] > word_list[j-1]:
        print(word_list[j])