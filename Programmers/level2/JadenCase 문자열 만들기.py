def solution(s):
    arr = s.split(' ')

    answer = []
    for i in range(len(arr)):
        if arr[i].isalpha():
            lower = arr[i].lower()
            s = lower[0].upper() + lower[1:]
            answer.append(s)
        else:
            answer.append(arr[i].lower())

    return ' '.join(answer)


# s = "3people unFollowed me"
# s = "for the last week"
s = "for the    last week"
print(solution(s))