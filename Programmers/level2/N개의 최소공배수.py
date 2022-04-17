def solution(arr):
    def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a % b)

    def lcd(a, b):
        return a * b // gcd(a, b)

    answer = arr[0]
    for x in arr:
        answer = lcd(answer, x)

    return answer


arr = [2, 6, 8, 14]
print(solution(arr))
