
# 답안처럼 풀이
def solution():

    grid = [list(map(int, input().split())) for _ in range(7)]

    cnt = 0
    for i in range(3):
        for j in range(7):
            tmp = grid[j][i:i + 5]
            if tmp == tmp[::-1]:
                cnt += 1

            for k in range(5 // 2):
                if grid[i + k][j] != grid[i + 4 - k][j]:
                    break
            else:
                cnt += 1

    return cnt


print(solution())