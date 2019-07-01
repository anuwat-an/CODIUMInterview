n = int(input())
for i in range(1,n//2+1):
    print(' '*(((n-1)//2)-i+1), end='')
    print('*'*((i-1)*2+1))

if n%2 != 0:
    print('*'*n)

for i in range(n//2, 0, -1):
    print(' '*(((n-1)//2)-i+1), end='')
    print('*'*((i-1)*2+1))
