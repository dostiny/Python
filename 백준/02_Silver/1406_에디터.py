import sys;

arr = list(sys.stdin.readline().rstrip())
idx = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'P':
        arr.append(command[1])
    elif command[0] == 'L':
        if arr:
            idx.append(arr.pop())
    elif command[0] == 'D':
        if idx:
            arr.append(idx.pop())
    else:
        if arr:
            arr.pop()

arr.extend(reversed(idx))
print(''.join(arr))