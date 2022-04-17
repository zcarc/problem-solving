def get_count(arr, mid):

    sum_len = 0
    cnt = 1

    for e in arr:
        if sum_len + e <= mid:
            sum_len += e

        elif sum_len + e > mid:
            sum_len = e
            cnt += 1

    return cnt


def solution():

    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    start = 1
    end = sum(arr)
    max_len = max(arr)

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = get_count(arr, mid)

        if mid >= max_len and cnt <= m:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer


print(solution())

# 9 3
# 1 2 3 4 5 6 7 8 9
# 위와 같은 입력이 주어졌을 때,
# 두번째로 입력되는 값들은 노래의 길이에 해당하고
# 1분부터 9분까지 있고 여기서 최대로 나올 수 있는 값은
# 전체 뮤직비디오 길이를 합산한 것이므로 45가 된다.
# 이분검색의 범위는 1 ~ 45 이다.
# 1 + 45 를 반으로 나누면 23
# 1,2,3,4,5,6 / 7,8 / 9 로 나눠서 더하면
# 21 / 15 / 9 가 되어 23 안에 포함되므로 3장으로 나누어진다.
# 여기서 답이 나왔지만 더 최적의 해를 구할 때까지 계속 찾는다.
