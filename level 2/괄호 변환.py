"""2020 KAKAO BLIND RECRUITMENT"""


def isBalance(p):
    """isBalance 균형잡힌 괄호인지 확인하는 함수

    Args:
        p (str): 괄호로만 이루어진 문자열

    Returns:
        [bool]: 균형잡힌 괄호인지 확인하여 리턴
    """
    if p.count("(") == p.count(")"):  # 괄호의 개수가 같으면 균형잡힌 괄호
        return True
    return False


def isCorrect(p):
    """isCorrect 올바른 괄호인지 확인하는 함수

    Args:
        p (str): 괄호로만 이루어진 문자열

    Returns:
        [bool]: 올바른 괄호인지 확인하여 리턴
    """
    stack = []
    for i in range(len(p)):
        # 비었거나 마지막이 닫는 괄호이거나 여는 괄호 후에 여는 괄호가 또 들어왔을 때
        if not stack or stack[-1] == ")" or (stack[-1] == "(" and p[i] == "("):
            stack.append(p[i])
        else:
            stack.pop()

    if not stack:  # 스택이 비었다면 올바른 괄호이다
        return True
    return False  # 비어있지 않다면 올바르지 않은 괄호다


def solution(p):
    """solution 올바른 괄호로 변경하는 함수

    Args:
        p (str): 괄호로만 이루어진 문자열

    Returns:
        answer (str): 올바른 괄호로 변경하여 리턴
    """
    answer = ""
    u = ""  # 균형잡힌 괄호의 최소 문자열
    v = ""  # u를 제외한 나머지 문자열

    if len(p) == 0 or isCorrect(p):  # 주어진 문자열이 비었거나 이미 올바른 괄호일 때
        return p

    for i in range(2, len(p) + 1, 2):  # 괄호는 쌍이므로 두 단위씩 확인해도 된다
        if isBalance(p[:i]):  # 균형잡힌 괄호이면 u, v를 지정하고 반복문 종료
            u = p[:i]
            v = p[i:]
            break

    if isCorrect(u):  # u가 올바른 괄호면
        answer += u + solution(v)  # answer에 더하고 남은 부분을 확인한다
    else:  # u가 올바른 괄호가 아니면
        answer += "(" + solution(v) + ")"  # 남은 부분 앞 뒤로 괄호를 붙이고
        for i in u[1:-1]:  # u의 맨 앞과 뒤를 제외한 나머지 괄호를 반대로 붙인다
            if i == "(":
                answer += ")"
            else:
                answer += "("

    return answer
