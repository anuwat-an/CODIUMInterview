import math

def isPrime(n):
    if n == 1 or (n > 2 and n%2 == 0):
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

n = int(input())
for i in range(2,n+1):
    if isPrime(i):
        print(i, end=' ')