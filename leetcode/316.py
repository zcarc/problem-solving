import collections

s = 'cbacdcbc'
s1 = 'cbacdcbcd'
s2 = 'eab'
s3 = 'eabe'
s4 = 'ecbacdcbc'


# 풀이 1. 재귀
def removeDuplicateLetters(s: str) -> str:
    print()
    print(f'start function... s: {s}')
    print(f'set(s): {set(s)}')
    print(f'sorted(set(s)): {sorted(set(s))}')

    for char in sorted(set(s)):
        print(f'for...')
        suffix = s[s.index(char):]
        print(f'suffix: {suffix}')
        print(f'char: {char}, s.index(char): {s.index(char)}')
        print(f'set(s): {set(s)}, set(suffix): {set(suffix)}')
        if set(s) == set(suffix):
            print(f'if... set(s) == set(suffix) is True')
            print(f'suffix.replace(char, \'\'): {suffix.replace(char, "")}')
            return char + removeDuplicateLetters(suffix.replace(char, ''))
        print()

    return ''


# print(f'result: {removeDuplicateLetters(s)}')
# print(f'result: {removeDuplicateLetters(s2)}')
# print(f'result: {removeDuplicateLetters(s3)}')
# print(f'result: {removeDuplicateLetters(s4)}')


def removeDuplicateLetters_Stack(s: str) -> str:
    stack = []

    print(f's: {s}')
    counter = collections.Counter(s)
    print(f'counter: {counter}')
    print(f"counter['c']: {counter['c']}")
    counter['c'] = counter['c'] - 1
    print("after counter['c'] = counter['c'] - 1")
    print(f"counter['c']: {counter['c']}")

    for char in s:
        stack.append(char)

    print(f'stack: {stack}')
    print(f'stack[-1]: {stack[-1]}')
    print(f'counter[stack[-1]]: {counter[stack[-1]]}')



# removeDuplicateLetters_Stack(s)




def removeDuplicateLetters_answer(s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            print(f'char: {char}, stack: {stack}')
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)


ss = 'bcabc'
print(removeDuplicateLetters_answer(ss))