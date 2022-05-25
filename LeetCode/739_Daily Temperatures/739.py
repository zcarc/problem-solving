def dailyTemperatures(temperatures):
    stack = []
    answer = [0] * len(temperatures)

    for i, cur in enumerate(temperatures):
        while stack and cur > temperatures[stack[-1]]:
            popped = stack.pop()
            answer[popped] = i - popped
        stack.append(i)

    print(f'stack: {stack}')

    return answer


print(dailyTemperatures([73,74,75,71,69,72,76,73]))