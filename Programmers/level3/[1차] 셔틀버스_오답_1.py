def solution(n, t, m, timetable):
    print(timetable)

    def to_minutes(e):
        h, m = map(int, e.split(':'))
        m += h * 60
        return m

    timetable = list(map(to_minutes, timetable))
    timetable.sort()

    stop_time = 540
    cnt = 0
    for i in range(0, len(timetable), m):
        for j in range(i, i + m):
            print(i, j, end=', ')
            if j <= len(timetable) - 1:
                print(timetable[j], stop_time)
                if stop_time >= timetable[j]:
                    cnt += 1
            else:
                break

        stop_time += t

    print()
    print(f'cnt: {cnt}')


# solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
