# 내 풀이.
def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    prevDays = sum(months[:a - 1])
    sumDays = prevDays + b

    return days[(sumDays - 1) % 7]


print(solution(1, 7))



