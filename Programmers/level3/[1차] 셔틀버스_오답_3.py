def solution(n, t, m, timetable):
    def to_minutes(e):
        h, m = map(int, e.split(':'))
        m += h * 60
        return m

    timetable = list(map(to_minutes, timetable))
    timetable.sort()

    tmp_m = m
    pointer = 0
    stop_time = 540
    on_bus = 0

    while pointer <= len(timetable) - 1 and n > 0:
        if tmp_m == 0:
            tmp_m = m
            n -= 1
            stop_time += t
            continue

        if stop_time >= timetable[pointer]:
            pointer += 1

        on_bus += 1
        tmp_m -= 1

    def to_hh_mm(minutes):
        hh = str(minutes // 60)
        mm = str(minutes % 60)

        if len(hh) == 1:
            hh = '0' + hh

        if len(mm) == 1:
            mm = '0' + mm

        return hh + ':' + mm

    if on_bus < n * m:
        if timetable[-1] < 540:
            return '09:00'
        else:
            return to_hh_mm(timetable[-1])
    else:
        if timetable[-1] == 1439:
            return '09:00'
        return to_hh_mm(timetable[-1] - 1)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
