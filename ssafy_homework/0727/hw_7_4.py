def collatz(num):
    count_up = 0
    while num != 1:
        if count_up == 500:
            return -1
        elif num%2 == 0:
            num = int(num/2)
            count_up += 1
        elif num%2 == 1:
            num = (num*3) + 1
            count_up += 1

    return count_up

print(collatz(6))