"""2021 KAKAO BLIND RECRUITMENT"""

possible = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "-",
    "_",
    ".",
]


def solution(new_id):
    answer = ""

    # 소문자로 변경
    new_id = new_id.lower()

    # 알파벳 소문자, 숫자, -, _, .를 제외하고 모두 제거
    set_new_id = ""
    for i in new_id:
        if i in possible:
            set_new_id += i

    # 마침표가 연속된 부분은 마침표 하나로 변경
    i = 0
    flag = 0
    while i < len(set_new_id):
        if flag:
            answer += "."
            flag = 0

        if set_new_id[i] != ".":
            answer += set_new_id[i]
        elif i + 1 <= len(set_new_id) - 1 and set_new_id[i + 1] != ".":
            flag = 1
        i += 1

    if flag:
        answer += "."
        flag = 0

    # 마침표가 처음이나 끝에 있다면 제거
    if len(answer) > 1:
        if answer[0] == ".":
            answer = answer[1:]
        if answer[-1] == ".":
            answer = answer[:-1]
    else:
        if answer == ".":
            answer = ""

    # 빈 문자열이라면 'a'를 대입
    if len(answer) == 0:
        answer += "a"

    # 길이가 16자리 이상이면 처음부터 15자리까지만 남김
    if len(answer) > 15:
        answer = answer[:15]
        if answer[14] == ".":
            answer = answer[:14]

    # 길이가 2자 이하라면 길이가 3이 될때까지 마지막 문자를 붙임
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]

    return answer


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))


# --------------------------------------------------------------------------------------------------------
"""단계별로 구현"""


def solution(new_id):
    answer = ""
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            answer += c
    # 3
    while ".." in answer:
        answer = answer.replace("..", ".")
    # 4
    if answer[0] == ".":
        answer = answer[1:] if len(answer) > 1 else "."
    if answer[-1] == ".":
        answer = answer[:-1]
    # 5
    if answer == "":
        answer = "a"
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer


# --------------------------------------------------------------------------------------------------------
"""정규 표현식 사용"""
import re


def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub("[^a-z0-9\-_.]", "", st)
    st = re.sub("\.+", ".", st)
    st = re.sub("^[.]|[.]$", "", st)
    st = "a" if len(st) == 0 else st[:15]
    st = re.sub("^[.]|[.]$", "", st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st
