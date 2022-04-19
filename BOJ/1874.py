import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
m = 0
stack = []
ans = ''

for x in a:
    if x > m:
        while x > m:
            m += 1
            stack.append(m)
            ans += '+\n'
        stack.pop()
        ans += '-\n'

    else:
        if stack[-1] != x:
            print('NO')
            sys.exit(0)
        stack.pop()
        ans += '-\n'

print(ans, end='')
