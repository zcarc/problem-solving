def solution(numbers):
    length = len(numbers)

    res = set()
    for i in range(length):
        for j in range(i + 1, length):
            res.add(numbers[i] + numbers[j])

    return sorted(list(res))


print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))