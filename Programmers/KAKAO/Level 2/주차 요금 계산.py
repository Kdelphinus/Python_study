"""2022 KAKAO BLIND RECRUITMENT"""

from math import ceil
from collections import defaultdict


def time_cal(out_time, in_time):
    out_hour = int(out_time.split(":")[0])
    out_minute = int(out_time.split(":")[1])
    in_hour = int(in_time.split(":")[0])
    in_minute = int(in_time.split(":")[1])

    out_time = out_minute + out_hour * 60
    in_time = in_minute + in_hour * 60

    return out_time - in_time


def solution(fees, records):
    answer = []
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    log = defaultdict(list)
    numbers = []
    for record in records:
        time, number, state = record.split()
        log[number].append([time, state])
        if number not in numbers:
            numbers.append(number)
    numbers.sort()

    for number in numbers:
        total_time = 0
        for time, state in log[number]:
            now = state
            if now == "IN":
                in_time = time
            else:
                total_time += time_cal(time, in_time)
        if now == "IN":
            total_time += time_cal("23:59", in_time)

        if total_time <= basic_time:
            fee = basic_fee
        else:
            total_time -= basic_time
            fee = basic_fee + ceil(total_time / unit_time) * unit_fee
        answer.append(fee)

    return answer


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]
print(solution(fees, records))
