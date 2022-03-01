from typing import List


def s(digits: str) -> List[str]:

    def dfs(index: int, combi: str):
        if len(combi) == len(digits):
            answer.append(combi)
            return

        for char in dic[digits[index]]:
            dfs(index + 1, combi + char)

    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    answer: List[str] = []

    dfs(0, '')

    return answer
