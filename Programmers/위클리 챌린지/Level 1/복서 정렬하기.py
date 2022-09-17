"""위클리 챌린지 6주차"""


def solution(weights, head2head):
    weights = list(enumerate(weights))
    players = []
    for i, w in weights:
        player = [i + 1, w, 0, 0]
        history = head2head[i]
        if history.count("W"):
            player[2] = history.count("W") / (len(history) - history.count("N"))
            for s in range(len(history)):
                if history[s] == "W" and w < weights[s][1]:
                    player[3] += 1
        players.append(player)

    players.sort(key=lambda x: (-x[2], -x[3], -x[1], x[0]))

    return [player[0] for player in players]


# 정렬 순서
# 1. 승률 / 2. 자신보다 몸무게가 무거운 복서를 이긴 횟수 / 3. 몸무게가 더 무거우면 / 4. 복서 번호
print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))  # [3, 4, 1, 2]
