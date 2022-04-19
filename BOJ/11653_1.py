n = int(input())

def findDivisors(n):
    l = []
    for i in range(1, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            l.append(i)
            l.append(n // i)
    l.sort()
    return l


def isPrime(n):
    if n == 1:
        return False

    for j in range(2, int(n ** (1 / 2)) + 1):
        if n % j == 0:
            return False
    else:
        return True

a = findDivisors(n)

primes = []
for i in a:
    if isPrime(i):
        primes.append(i)

tmp = n

for i in primes:
    while tmp % i == 0:
        tmp = tmp // i
        print(i)
