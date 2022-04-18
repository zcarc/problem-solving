from string import ascii_uppercase


def solution(name):

    len_name = len(name)
    sum_up_down = 0

    move_left_right = []

    # 한 방향으로 쭉 갔을 때
    move_left_right.append(len_name - 1)

    # 알파벳 위,아래 계산
    for i in range(len_name):
        index_alphabet = ascii_uppercase.index(name[i])
        sum_up_down += min(index_alphabet, len(ascii_uppercase) - index_alphabet)

    # 알파벳 왼쪽,오른쪽 계산
    for i in range(len_name):
        end_A = i + 1
        while end_A < len_name and name[end_A] == 'A':
            end_A += 1

        print(f'i: {i}, end_A: {end_A}')

        move_to_start_A, move_to_end_A = i, len_name - end_A
        print(f'move_to_start_A: {move_to_start_A}, move_to_end_A: {move_to_end_A}')
        print(f' i({i}) + i({i}) + (len_name({len_name}) - end_A({end_A})) = {i + i + (len_name - end_A)}')
        print(f' (len_name({len_name}) - end_A({end_A})) + (len_name({len_name}) - end_A({end_A})) + i({i}) = {(len_name - end_A) + (len_name - end_A) + i}')
        move_left_right.append(move_to_start_A + move_to_start_A + move_to_end_A)  # 0 -> A.., 0 <- A.., ..A <- -1
        move_left_right.append(move_to_end_A + move_to_end_A + move_to_start_A)  # 뒤에서 시작할 경우 ..A <- -1, ..A -> -1, 0 -> A..

        print(move_left_right)
        print()

    print(f'sum_up_down: {sum_up_down}')
    print(f'min(move_left_right): {min(move_left_right)}')

    return sum_up_down + min(move_left_right)


# print(solution(['B', 'A', 'C']))
# print(solution(['B','C','D']))
print(solution(['B','C','D','E','F','G']))
# print(solution(['B', 'C', 'A', 'A', 'E']))
# print(solution(['B','B','A','C','D']))
# print(solution(['B', 'B', 'B', 'A', 'A', 'C', 'D']))
# print(solution(['L','A','A','B','A','A']))
# print(solution(['L','A','B','L','P','A','J','M']))  # 55 (위,아래 합계)
# print(solution(['L','A','A','B','L','P','A','J','M','A','A']))
# print(solution(['L','A','A','B','L','P','A','J','M','A','A','A']))
# print(solution(['B','B','B','B','A','A','A','A','A','B']))


# 설명
# 한쪽 방향으로만 가는 경우
# ['B','C','D','E','F','G']
# 이 경우는 'A'가 없으므로 최소거리가 시작과 동시에 오른쪽 한쪽 방향으로만 가는 경우가 최소거리가 된다.
# 'A'가 존재하면 end_A가 증가하게 되는데 len(name)에 이 증가한 end_A를 빼줘야 최소거리가 나오기 때문에
# 'A'가 존재하지 않으므로 len(name) - end_A를 하면 최소거리를 찾을 수 없다.

# move_to_start_A + move_to_start_A + move_to_end_A
# 이 부분을 설명하면 name = ['B', 'B', 'B', 'A', 'A', 'C', 'D'] / i = 2 일 때,

# 시작 i (0)부터 현재 i (2)까지 이동한 거리는 다음과 같다.
# => move_to_start_A

# 그 거리 i (2)에서 다시 시작지점 i (0)으로 되돌아가고, 인덱스 0 지점부터 인덱스의 끝인 오른쪽으로 이동하고,
# 거기서부터 왼쪽으로 이동하면서 조건을 만족해서 처음에 발견된 연속되는 'A'의 다음 인덱스 (5)까지 이동해야하므로 다음과 같다.
# => + move_to_start_A + move_to_end_A


# name에 'A'가 연속적으로 포함되어 있다면
# 'A' 직전의 문자에서 다음 'A'가 있는 지 확인하니까
# 다음 코드가 True가 되고 'A' 마지막 위치 다음 문자에서 멈추게 된다.
# 여기서 모든 문자가 각각 오른쪽으로 이동했다가 다시 왼쪽으로 이동하는 최소 거리가 move_left_right 리스트에 담기게 된다.
# while end_A < len_name and name[end_A] == 'A':
#     end_A += 1


# 테스트케이스 ['L','A','B','L','P','A','J','M'] 인 경우
# 처음에 'L'에서 오른쪽으로 갔다가 'A'를 발견해서 왼쪽으로 간다 그러면
# 인덱스 7부터 2까지 왼쪽으로 이동하는데
# 'L' -> 'A' -> 'B'로 가는 것이 'L' -> 'M' -> 'J' 이런순으로 가는것 보다 빠르지 않을까? 라는 생각을 했으나
# 'L' 다음에는 'A'가 있고 그래서 뒤로 이동하는데 여기서 만약 뒤로 이동하지 않고 앞으로 이동한다면
# 뒤로 이동했을 때는 총 이동거리가 6이 되는데 앞으로 이동했을 때는 앞의 'A' 때문에 이동거리가 7이 된다.

# ['L','A','A','B','L','P','A','J','M']
# 여기서는 'L' 다음에 'A', 'A' 로 연속해서 2개 나오는데 앞으로 이동한다면 총 이동거리는 8이 되고
# 뒤로 이동하게 된다면 이동거리는 6이 된다.

# ['L','A','A','B','L','P','A','J','M','A','A']
# => 오른쪽의 'A'가 2개 있고 왼쪽에 'A'가 두개 있으나 둘다 같은 값이므로 최소 이동거리는 8


# 뒤에서 시작할 경우가 최소거리인 경우
# 예시 1.
# ['L','A','A','B','L','P','A','J','M','A','A','A'], i = 8
# 이 경우는 'L' -> 'A'를 찾았고 뒤로 이동해서
# 'L' -> 'A','A','A','M','J','A','P','L','B' 이동거리가 9가 되는데
# 인덱스 8에서 다음 문자가 'A'가 발견되어 인덱스 9 ~ 11에 있는 'A', 'A', 'A' 만큼 이동하고 다시 그 만큼 오른쪽으로 이동한다음
# 거기서 또 오른쪽으로 이동하게 된다.
# 시작: 끝 인덱스에서 왼쪽으로 이동 11 -> 10 -> 9 (2번)
# 다시 오른쪽으로 이동 9 -> 10 -> 11 (2번)
# 마지막 문자들은 'A'이기 때문에 사실상 이동횟수는 0이 된다.
# 거기서 i 만큼 이동한다면 문자 'M'을 만나게 된다.
# 그래서 인덱스 0부터 8까지 이동하게 되어 최소거리는 8이 된다.
# len(12) - end_A(12) + i(8) = 8

# 예시 2.
# ['B','B','B','B','A','A','A','A','A','B']
# 이 경우에는 i = 3 일 때, 그 다음 문자가 'A'가 되고 총 5번 반복을 해서 시작과 끝 인덱스가 4 ~ 8이 된다.

# 마지막 인덱스가 왼쪽으로 이동한다 ...A < -1
# => len(number) - end_A

# 왼쪽으로 이동한 인덱스가 이동한만큼 다시 오른쪽으로 이동한다 ... A -> -1
# => + len(number) - end_A

# 끝에서 시작했으므로 거기서부터 이동해야하기 때문에 i 만큼 이동한다.
# => + i

# i: 3, end_A: 9
# (len_name(10) - end_A(9)) + (len_name(10) - end_A(9)) + i(3) = 5
# => 그래서 최소 이동거리는 5가 된다.


# 참고
# https://excited-hyun.tistory.com/207
# https://velog.io/@jeeseob5761/프로그래머스-조이스틱
# https://programmers.co.kr/questions/27706
# https://programmers.co.kr/questions/29742
# https://programmers.co.kr/questions/25695