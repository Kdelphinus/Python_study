from collections import deque


def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque()  # 사용할 스택 정의
    close_list = []
    for i in string:
        stack.append(i)
    while len(stack) != 0:
        data = stack.pop()
        if data == ")":
            close_list.append(len(stack))
        elif data == "(":
            index_open = len(stack)
            if close_list:
                close_list.pop()
            else:
                print(f"문자열 {index_open} 번째 위치에 있는 괄호가 닫히지 않았습니다")
    if close_list:
        close_list.sort()
        for index in close_list:
            print(f"문자열 {index} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다")


case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)

# ---------------------------------------------------------------------------------------------
print("\n\n모범답안\n\n")


def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    stack = deque()  # 사용할 스택 정의

    print(f"테스트하는 문자열: {string}")

    # 문자열의 각 문자를 돌면서
    for i in range(len(string)):
        # 열리는 괄호가 있는 위치를 스택에 저장
        if string[i] == "(":
            stack.append(i)
        # 닫히는 괄호가 있으면
        elif string[i] == ")":
            # 스택에 열린 괄호 위치 데이터가 있으면 삭제하고
            if stack:
                stack.pop()
            # 아니면 현재 위치에 있는 닫는 괄호에 맞는 괄호가 없다고 출력
            else:
                print(f"문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 여는 괄호가 없습니다")

    # 스택에 열린 괄호 위치 데이터가 남아 있으면 해당 열린 괄호는 짝이 맞는 닫힌 괄호가 없다는 뜻
    while stack:
        print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")


case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)