"""4949 균형잡힌 세상"""
import sys

while True:
    string = sys.stdin.readline().rstrip()

    if string == ".":
        break

    string = list(string)
    check_small = 0  # 소괄호 확인
    check_big = 0  # 대괄호 확인
    check = []  # 먼저 닫아야 할 괄호를 저장할 리스트

    while True:
        tem_string = string.pop()  # 확인하면서 여러개가 빠지지 않도록 빼고 변수로 지정
        if tem_string == "(" or tem_string == "[":  # 괄호를 닫아야 할 때
            if not check:  # 닫을 괄호가 없다면
                print("no")
                break
            tem_check = check.pop()

        if tem_string == ")":
            check_small += 1
            check.append(0)
        elif tem_string == "(":
            if tem_check == 1:  # 현재 닫아야 할 괄호가 []라면
                print("no")
                break
            else:
                check_small -= 1
        elif tem_string == "]":
            check_big += 1
            check.append(1)
        elif tem_string == "[":
            if tem_check == 0:  # 현재 닫아야 할 괄호가 ()라면
                print("no")
                break
            else:
                check_big -= 1

        if not string:  # 문자열을 다 봤다면
            if check_big == 0 and check_small == 0:
                print("yes")
            else:
                print("no")
            break
