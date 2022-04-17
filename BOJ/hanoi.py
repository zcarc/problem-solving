# 2021.11.23
# 하노이의 탑

# 2022.01.15 수정
# 1914번 문제로 새로 풀었으니 이 풀이 대신 그 풀이로 풀이한다.

n = int(input())

# 총 반복하는 횟수: 2^n - 1
print(2 ** n - 1)

def hanoi(n, start, mid, to):
    if n == 1:
        print(f'{start} {to}')
        return

    # step 1: A -> B
    hanoi(n-1, start, to, mid)

    # step 2: A -> C
    print(f'{start} {to}')

    # step 3: B -> C
    hanoi(n-1, mid, start, to)


hanoi(n, 1, 2, 3)