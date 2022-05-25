import sys

# 풀이 1. 브루트 포스
def s(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# print(s([7,1,5,3,6,4]))
print()

# 풀이 2. 저점과 현재 차이 계산
def s2(prices):
    profit = 0
    min_price = sys.maxsize

    # 최소값과 최대값 계속 갱신
    for price in prices:
        print(f'min_price({min(min_price, price)}) = min(min_price({min_price}), price({price}))')
        min_price = min(min_price, price)

        print(f'profit({max(profit, price - min_price)}) = max(profit({profit}), price({price}) - min_price({min_price})({price - min_price}))')
        profit = max(profit, price - min_price)
        print()

    return profit


print(s2([7,1,5,3,6,4]))

# print(s2([6,5,4,3,2]))