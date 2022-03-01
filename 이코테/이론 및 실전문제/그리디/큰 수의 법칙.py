n, m, k, = map(int, input().split())
numbers = input()


def solution(numbers, m, k):

    array = list(map(int, numbers.split(' ')))
    array.sort(reverse=True)
    array = array[:2]
    total = 0

    for i in range(1, m + 1):
        if i % k == 0:
            print(array[1])
            total += array[1]
        else:
            print(array[0])
            total += array[0]

    return total


# print(solution(numbers, m, k))


# 책 풀이
# m의 크기가 100억 이상처럼 커지면 시간초과를 받을 수 있어서 다른 풀이가 필요하다.
def solution2(numbers, m, k):

    answer = 0

    array = list(map(int, numbers.split(' ')))
    array.sort(reverse=True)
    array = array[:2]

    # 반복되는 수열은 k + 1 이므로, 총 반복 횟수(m) / 반복 수열(k + 1)
    # 하나의 수열이 반복되는 횟수를 구함
    count = m // (k + 1)

    # 연속 가능한 반복 횟수(K) * 첫번째와 두번째 큰 수가 포함된 수열의 묶음
    # 연속 가능한 반복 횟수는 결국 수열에서 첫번째로 큰 수
    count = k * count

    # 수열의 묶음에서 나눠지지 않은 나머지
    # 즉, 두번째로 큰 수가 포함되지 않은 수열
    # count에는 총 수열에서 가장 큰 수의 개수가 저장됨
    count *= m % (k + 1)

    print(count)
    print(array)

    # 첫번째로 큰 수의 개수 * 첫번째로 큰 수
    answer += count * array[0]

    # 두번째로 큰 수의 개수(총 반복 횟수 - 첫번째로 큰 수의 개수) * 두번째로 큰 수
    answer += (m - count) * array[1]

    return answer


print(solution2(numbers, m, k))