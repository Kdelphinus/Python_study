"""2020 카카오 인턴십"""


def solution(numbers, hand):
    answer = ""
    right = [2, 3]  # 오른손 시작 위치
    left = [0, 3]  # 왼손 시작 위치
    position = [  # position[index]: index 번호의 위치
        [1, 3],
        [0, 0],
        [1, 0],
        [2, 0],
        [0, 1],
        [1, 1],
        [2, 1],
        [0, 2],
        [1, 2],
        [2, 2],
    ]

    for num in numbers:  # 눌러야 할 번호를 순서대로 본다
        goal = position[num]  # 가야할 위치
        if goal[0] == 0:  # 왼쪽에 있는 번호면
            answer += "L"  # 왼쪽을 더하고
            left = position[num]  # 그 위치로 왼손 이동
        elif goal[0] == 2:  # 오른쪽에 있는 번호면
            answer += "R"  # 오른쪽을 더하고
            right = position[num]  # 그 위치로 오른손 이동
        else:  # 가운데 있다면
            dist_left = abs(left[0] - goal[0]) + abs(left[1] - goal[1])  # 왼손이 이동할 거리
            dist_right = abs(right[0] - goal[0]) + abs(
                right[1] - goal[1]
            )  # 오른손이 이동할 거리

            if dist_left > dist_right:  # 오른손이 더 가깝다면 오른손 이동
                answer += "R"
                right = position[num]
            elif dist_right > dist_left:  # 왼손이 더 가깝다면 왼손 이동
                answer += "L"
                left = position[num]
            else:  # 위치가 같다면 오른손 잡이는 오른손, 왼손잡이는 왼손 이동
                if hand == "right":
                    answer += "R"
                    right = position[num]
                else:
                    answer += "L"
                    left = position[num]

    return answer
