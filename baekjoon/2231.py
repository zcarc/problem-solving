
def findConstructor(n):
    result = 0

    for i in range(n):
        number = i
        s = 0

        while number != 0:
            s = s + (number % 10)
            number = number // 10

        if s + i == n:
            result = i
            break

    return result


n = int(input())

print(findConstructor(n))