def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index

    return max_length


def lengthOfLongestSubstring2(s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length


# s = "tmmzuxt"
# s = "tmzuxtabc"
# s = "abcb"
# s = "abcbabc"
s = "nfpdmpi"
print(lengthOfLongestSubstring(s))
print(lengthOfLongestSubstring2(s))