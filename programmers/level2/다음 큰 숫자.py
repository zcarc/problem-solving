def solution(n):
    bigger = n
    for num in range(n, 1000000 + 1):
        bigger += 1

        bin_n = bin(n)[2:]
        bin_bigger = bin(bigger)[2:]

        if bin_n.count('1') == bin_bigger.count('1'):
            return bigger