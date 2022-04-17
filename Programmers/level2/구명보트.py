# 풀이 1.
def solution(people, limit):

    people.sort()

    start = 0
    end = len(people) - 1

    answer = 0

    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1
        end -= 1

    return len(people) - answer


# 풀이 1번이 더 괜찮다.
# 이 경우는 비교하는 대상이 서로 달라야하므로 start < end 조건이다.


# 풀이 2.
def solution2(people, limit):

    people.sort()

    start = 0
    end = len(people) - 1
    answer = 0

    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return answer


# 이 경우는 비교대상이 서로 같을 수도 있다.
# 이유는 answer을 계속 증가해야 하는데
# 마지막 더 큰수의 조건이라면 자기자신은 호출하지 못한다.
# 나는 개인적으로 풀이 1번이 더 괜찮은 것 같다.