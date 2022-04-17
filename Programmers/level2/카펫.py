def solution(brown, yellow):

    total = brown + yellow

    for i in range(1, total + 1):
        if total % i == 0:
            height = i
            width = total // height
            center = (height - 2) * (width - 2)
            if center == yellow:
                return [width, height]


print(solution(10, 2))
print(solution(8, 1))


# 참고:
# https://mungto.tistory.com/43