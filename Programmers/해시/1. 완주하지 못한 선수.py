"""나의 풀이"""


# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i in range(len(participant)):
#         if len(completion) == i:
#             return participant[i]
#         elif completion[i] != participant[i]:
#             return participant[i]


"""모범 답안"""
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    print(answer)
    print(list(answer.keys()))

    return list(answer.keys())[0]


a = ["명준", "주경", "윤우"]
b = ["명준", "주경"]

print(solution(a, b))
