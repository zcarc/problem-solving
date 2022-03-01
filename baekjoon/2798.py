def blackjack_search(n, m, numbers):
    notEqualSum = 0

    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sumNumbers = numbers[i] + numbers[j] + numbers[k]
                if m == sumNumbers:
                    return m

                if notEqualSum < sumNumbers < m:
                    notEqualSum = sumNumbers

    return notEqualSum


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

result = blackjack_search(n, m, numbers)
print(result)
