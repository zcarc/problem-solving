# 내 풀이.
def solution(array, commands):

    answer = []

    for oneDimensional in commands:
        i = oneDimensional[0]
        j = oneDimensional[1]
        k = oneDimensional[2]
        sortedArray = sorted(array[i - 1:j])
        targetNumber = sortedArray[k - 1]
        answer.append(targetNumber)

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))


# 다른사람 풀이

# 풀이 1.
def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))