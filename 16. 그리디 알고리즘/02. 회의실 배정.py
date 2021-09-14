"""1931 회의실 배정"""

num = int(input())  # 회의 수
conferences = sorted(
    [list(map(int, input().split())) for _ in range(num)], key=lambda x: (x[0], x[1])
)  # 회의 시작시간, 끝나는 시간
pass_con = []  # 회의실 사용 가능한 회의

for conference in conferences:
    if len(pass_con) == 0:  # 첫 예약시간 입력
        pass_con.append(conference)
    else:
        if (
            pass_con[-1][1] <= conference[0]
        ):  # 마지막으로 예약된 끝나는 시간 <= 예약하려는 시작 시간 이면 예약에 추가한다
            pass_con.append(conference)
        elif (
            pass_con[-1][1] > conference[1]
        ):  # 마지막으로 예약된 시간보다 더 일찍 끝나는 회의이면 마지막 회의를 바꾼다
            pass_con[-1] = conference

print(len(pass_con))
