"""위클리 챌린지 4주차"""


def solution(table, languages, preference):
    scores = []
    for i in range(len(table)):
        scores.append(list(table[i].split()))

    table = []
    for i in range(len(scores)):
        total = 0
        for idx in range(len(languages)):
            if languages[idx] in scores[i]:
                total += (6 - scores[i].index(languages[idx])) * preference[idx]
        table.append([scores[i][0], total])
    table.sort(key=lambda x: (-x[1], x[0]))

    return table[0][0]


table = [
    "SI JAVA JAVASCRIPT SQL PYTHON C#",
    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
    "GAME C++ C# JAVASCRIPT C JAVA",
]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
print(solution(table, languages, preference))
