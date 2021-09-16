"""위클리 챌린지 7주차"""


def solution(enter, leave):
    answer = [0] * len(enter)
    room = []
    enter_idx = 0

    for l in leave:
        while l not in room:  # 퇴실할 사람이 들어올 때까지 입실
            room.append(enter[enter_idx])
            enter_idx += 1

        room.remove(l)  # 퇴실할 사람이 퇴실
        for r in room:  # 방에 있는 사람들끼리는 무조건 만난다
            answer[r - 1] += 1
        answer[l - 1] += len(room)  # 퇴실한 사람은 퇴실 직전 같이 있던 사람과 만난다

    return answer
