def dbssus(n):
    result = ''
    if n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        result = 'true'
    elif n % 4 == 0 and n % 100 == 0:
        result = 'false'
    elif n % 4 == 0:
        result = 'true'
    else:
        result = 'false'
    return result

n = int(input())

print(dbssus(n))