n = int(input())
print(' '*(n-1), end='')
print('*')
for i in range(1, n):
    print(' '*(n-1-i), end='')
    print('*',end='')
    print(' '*((i-1)*2+1), end='')
    print('*')
