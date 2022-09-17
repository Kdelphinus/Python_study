"""Summer/Winter Coding(~2018)"""


def solution(n, words):
    answer = [0, 0]
    idx = 1
    check = []
    check.append(words[0])
    while idx < len(words):
        # 전 단어의 마지막 알파벳과 현 단어의 시작 알파벳이 다르거나 이미 말했던 단어일 때
        if words[idx - 1][-1] != words[idx][0] or words[idx] in check:
            return [idx % n + 1, idx // n + 1]
        check.append(words[idx])
        idx += 1

    return answer


# --------------------------------------------------------------------------------------
"""같은 원리, 다른 구현"""


def use_for(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p - 1][-1] or words[p] in words[:p]:
            return [p % n + 1, p // n + 1]
        else:
            return [0, 0]


print(
    solution(
        3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    )
)  # [3, 3], 3번째 순서 사람이 3번째 차례에서 틀림

print(
    solution(
        3,
        [
            "hello",
            "observe",
            "effect",
            "take",
            "either",
            "recognize",
            "encourage",
            "ensure",
            "establish",
            "hang",
            "gather",
            "refer",
            "reference",
            "estimate",
            "executive",
        ],
    )
)  # [0, 0], 틀린 사람 없음
