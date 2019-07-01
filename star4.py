n = int(input())
for i in range(1, (n//2)+1):
    print(' '*(i-1), end='')
    print('*', end='')
    print(' '*(n-(i*2)), end='')
    print('*')
if n%2 != 0:
    print(' '*(n//2), end='')
    print('*')
for i in range(n//2, 0, -1):
    print(' '*(i-1), end='')
    print('*', end='')
    print(' '*(n-(i*2)), end='')
    print('*')
