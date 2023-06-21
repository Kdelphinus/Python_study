"""2018 KAKAO BLIND RECRUITMENT"""


# 풀이: https://mjmjmj98.tistory.com/127
def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt


def solution(lines):
    answer = 0
    log = []  # log의 (시작시간, 끝시간) 저장

    for line in lines:
        date, s, t = line.split()
        s = s.split(":")
        t = t.replace("s", "")

        # 시간을 msec 단위로 저장
        end = (int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2])) * 1000
        start = end - float(t) * 1000 + 1
        log.append([start, end])

    # 각 작업의 시작 시간을 기준으로 1초로 끊어 확인
    for x in log:
        answer = max(
            answer,
            throughput(log, x[0], x[0] + 1000),
            throughput(log, x[1], x[1] + 1000),
        )

    return answer


######################################################################################################

"""내가 한 풀이 / 77.3"""
# from collections import defaultdict
#
# basic_time = 0
#
#
# def time_cal(start_time, end_time, idx):
#     global basic_time
#
#     if idx == 0:
#         basic_time = start_time[2] - int(start_time[2])
#     working = []
#     if end_time[2] > start_time[2]:
#         for n in range(int(start_time[2]), int(end_time[2]) + 1):
#             working.append(
#                 ":".join([str(start_time[0]), str(start_time[1]), str(n + basic_time)])
#             )
#     else:
#         for n in range(int(start_time[2]), 60):
#             working.append(
#                 ":".join([str(start_time[0]), str(start_time[1]), str(n + basic_time)])
#             )
#         for n in range(0, int(end_time[2]) + 1):
#             working.append(
#                 ":".join([str(end_time[0]), str(end_time[1]), str(n + basic_time)])
#             )
#
#     return working
#
#
# def time_duration(time, duration):
#     duration = float(duration[:-1])
#     hour, minute, second = time.split(":")
#     hour, minute, second = int(hour), int(minute), float(second)
#     if second >= duration:
#         second -= duration
#     else:
#         second = 60 - (duration - second)
#         if minute == 0:
#             minute = 59
#             hour -= 1
#         else:
#             minute -= 1
#
#     return hour, minute, second
#
#
# def solution(lines):
#     timeline = defaultdict(int)
#     timeline["0"] = 0
#
#     for idx, line in enumerate(lines):
#         date, time, duration = line.split()
#         start_time = list(time_duration(time, duration))
#         end_hour, end_minute, end_second = time.split(":")
#         end_time = [int(end_hour), int(end_minute), float(end_second)]
#         working = time_cal(start_time, end_time, idx)
#
#         for work in working:
#             timeline[work] += 1
#     print(timeline)
#     return max(timeline.values())


print(solution(["2016-09-15 23:59:59.999 0.001s"]))
