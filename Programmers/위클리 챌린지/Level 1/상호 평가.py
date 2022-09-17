"""위클리 챌린지 2주차"""


def grade(mean):
    if mean >= 90:
        return "A"
    elif mean >= 80:
        return "B"
    elif mean >= 70:
        return "C"
    elif mean >= 50:
        return "D"
    return "F"


def solution(scores):
    answer = ""

    for i in range(len(scores)):
        score = []
        for j in range(len(scores[i])):
            score.append(scores[j][i])

        if (max(score) == score[i] or min(score) == score[i]) and score.count(
            score[i]
        ) == 1:
            answer += grade((sum(score) - score[i]) / (len(score) - 1))
        else:
            answer += grade(sum(score) / len(score))

    return answer
