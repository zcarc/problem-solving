position = int(input())

current_line = 0
accumulate_sum_line = 0

while True:
    if position > current_line + accumulate_sum_line:
        accumulate_sum_line += current_line
    elif position <= current_line + accumulate_sum_line:
        if current_line % 2 == 1:
            print(f'{current_line - (position - accumulate_sum_line) + 1}/{position - accumulate_sum_line}')
        elif current_line % 2 == 0:
            print(f'{position - accumulate_sum_line}/{current_line - (position - accumulate_sum_line) + 1}')
        break
    current_line += 1
