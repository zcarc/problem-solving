def solution(skill, skill_trees):
    len_skill = len(skill)

    ch = [0] * len_skill

    cnt = 0
    for e in skill_trees:
        flag = False
        ch = [0] * len_skill
        for char in e:
            if char in skill:
                index_char = skill.index(char)
                ch[index_char] = 1
                for i in range(len(skill[:index_char])):
                    if ch[i] == 0:
                        flag = True
                        break

                if flag:
                    break

        if flag is False:
            cnt += 1

    return cnt


# print(solution("CBD", ["CBADF"]))
# print(solution("CBD", ["BDA"]))
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


