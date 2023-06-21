from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 1  # 처음 다리로 올라갈 때 1초의 시간이 걸림
    bridge = deque()  # 다리에 올라간 트럭의 무게
    bridge.append([1, truck_weights.popleft()])  # [진입한 시간, 트럭 무게]

    if not truck_weights:  # 만약 한대만 있었다면 다리 길이 + 1초 걸림
        return bridge_length + 1

    while True:
        answer += 1  # 1초 시간이 지나고
        total_weight = 0
        cnt = 0

        for i in range(len(bridge)):  # 다리를 다 건넌 트럭을 빼줌
            if answer - bridge[i][0] == bridge_length:
                bridge.popleft()
                break

        for i in bridge:  # 다리 위 트럭의 무게를 구함
            total_weight += i[1]

        if (
            truck_weights and total_weight + truck_weights[0] <= weight
        ):  # 트럭이 더 올라갈 수 있으면 올림
            bridge.append([answer, truck_weights.popleft()])

        if not truck_weights and not bridge:  # 모든 트럭이 지나가면 시간 출력
            return answer


# 테스트 코드
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
