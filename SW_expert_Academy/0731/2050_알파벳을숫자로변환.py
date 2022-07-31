input_head = input()

if len(input_head) <= 80:
    input_head = input_head.split('_')
    input_head = [i.lower() for i in input_head]
    print('_'.join(input_head))