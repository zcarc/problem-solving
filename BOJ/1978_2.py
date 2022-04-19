input()
b = list(map(int, input().split()))

cnt = 0

# 제곱근 사용
# 시간복잡도: O(root n)
def isPrime(n):
    if n == 1:
        return False

    for j in range(2, int(n ** (1/2)) + 1):
        if n % j == 0:
            return False
    else:
        return True

for i in b:
    if isPrime(i):
        cnt += 1

print(cnt)
