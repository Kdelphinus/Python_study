"""월간 코드 챌린지 시즌 2"""
from collections import deque


def isRight(string):
    stack = []
    for s in string:
        if not stack or s == "[" or s == "(" or s == "{":
            stack.append(s)
        elif s == "]" and stack[-1] == "[":
            stack.pop()
        elif s == ")" and stack[-1] == "(":
            stack.pop()
        elif s == "}" and stack[-1] == "{":
            stack.pop()

    if stack:
        return False
    return True


def solution(s):
    answer = 0
    string = deque(s)
    for x in range(len(s)):
        if isRight(string):
            answer += 1
        tmp = string.popleft()
        string.append(tmp)

    return answer


print(solution("{}()[]"))  # 3
print(solution("}]()[{"))  # 2
print(solution("[)(]"))  # 0
print(solution("{{{"))  # 0
