n = int(input())

top_range = n//2+2
if n <= 2:
    top_range -= 1
for i in range(1, top_range):
    print('A'*(n-i), end='')
    print('+', end='')
    print('E'*((i-2)*2+1), end='')
    if ((i-2)*2+1 > 0):
        print('+', end='')
    print('B'*(n-i))

for i in range(top_range, 0, -1):
    print('C'*(n-i), end='')
    print('+', end='')
    print('E'*((i-2)*2+1), end='')
    if ((i-2)*2+1 > 0):
        print('+', end='')
    print('D'*(n-i))
