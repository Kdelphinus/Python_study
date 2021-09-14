"""2017 팁스타운"""


def solution(s):
    stack = []
    if len(s) < 2:  # 길이가 2보다 작으면 짝지을 문자가 없다
        return 0

    for i in s:
        if len(stack) == 0:  # stack에 아무것도 없다면 문자를 넣는다
            stack.append(i)
        elif stack[-1] == i:  # stack 끝 문자와 현재 문자가 같다면 stack에서 제거
            stack.pop()
        else:  # 같지 않다면 추가
            stack.append(i)

    if stack:  # stack에 문자가 남아있다면 실패
        return 0
    return 1  # 비어있다면 성공


print(solution("cdcd"))
