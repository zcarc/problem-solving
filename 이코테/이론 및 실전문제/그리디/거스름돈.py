# 내가 쓴 답
def solution(n, coin_types):

    count = 0
    for coin_type in coin_types:
        count = count + (n // coin_type)
        n = n % coin_type

    return count


print(solution(1260, [500, 100, 50, 10]))


# 책의 풀이.
def solution2():

    n = 1260
    coin_types = [500, 100, 50, 10]
    count = 0

    for coin_type in coin_types:
        count += (n // coin_type)
        n = n % coin_type

    return count


# 화폐의 종류가 K개 라고 할 때,
# 시간 복잡도는 O(K)이다.