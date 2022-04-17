from typing import List


def letterCombinations(digits: str) -> List[str]:
    def dfs(index, path):
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        for i in dic[digits[index]]:
            print(f'dic[digits[index]]: {dic[digits[index]]}')
            print(f'digits[index]: {digits[index]}')
            print(f'dic[digits[0]]: {dic[digits[0]]}')
            print(f'dic["2"]: {dic["2"]}')
            dfs(index + 1, path + i)

    # 예외 처리
    if not digits:
        return []

    dic = {"2": "ab", "3": "de", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    dfs(0, "")

    return result


print(letterCombinations("2"))
