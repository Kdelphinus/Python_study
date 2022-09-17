def solution(s):
    answer = True
    stack = []
    for i in s:
        if not stack or i == "(":
            stack.append(i)
        elif i == ")":
            stack.pop()
    if stack:
        return False
    return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
