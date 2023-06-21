"""2020 카카오 인턴십"""
import copy


def solution(expression):
    answer = 0
    operators = ["*+-", "*-+", "+-*", "+*-", "-*+", "-+*"]

    # expression을 부호와 숫자로 나누어 리스트에 저장
    expression = expression.replace("+", " + ")
    expression = expression.replace("-", " - ")
    expression = expression.replace("*", " * ")
    expression = expression.split()

    for oper in operators:
        tmp = copy.deepcopy(expression)  # 리스트 복사
        for i in range(2):
            while True:
                try:  # 아직 먼저 연산할 부호가 있을 때
                    idx = tmp.index(oper[i])
                    string = str(tmp[idx - 1] + tmp[idx] + tmp[idx + 1])
                    tmp[idx + 1] = str(eval(string))
                    del tmp[idx - 1]  # 앞 숫자 제거
                    del tmp[idx - 1]  # 부호 제거, 인덱스가 하나씩 앞으로 당겨지기 때문
                except:  # 없다면
                    break
        answer = max(answer, abs(eval("".join(tmp))))

    return answer


print(solution("100-200*300-500+20"))

# ----------------------------------------------------------------------------------------------


# 우선순위를 역순으로 구한 방법
def solution(expression):
    operations = [
        ("+", "-", "*"),
        ("+", "*", "-"),
        ("-", "+", "*"),
        ("-", "*", "+"),
        ("*", "+", "-"),
        ("*", "-", "+"),
    ]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f"({b.join(temp)})")
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
