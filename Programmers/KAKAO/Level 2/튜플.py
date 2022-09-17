"""2019 카카오 개발자 겨울 인턴십"""

from collections import Counter


def s_to_i(s):
    """s_to_i 문자열에서 숫자만 뽑아냄

    Args:
        s (str): 주어진 문자열

    Returns:
        number (list): 숫자만 담긴 리스트
    """
    number = []
    num = ""
    i = 0
    while i < len(s) - 1:
        if s[i].isdigit():  # 숫자일 때
            num += s[i]  # 우선 문자열에 더하고
            while s[i + 1].isdigit():  # 다음 문자도 숫자면 숫자가 안 나올 때까지 쭉 더한다
                num += s[i + 1]
                i += 1
            number.append(int(num))  # 구한 숫자를 int로 바꾸어 저장
            num = ""
        i += 1

    return number


def solution(s):
    numbers = Counter(s_to_i(s))  # 구한 원소들의 개수를 구하여 저장
    print(numbers)
    print(numbers.items())
    return list(
        map(int, [k for k, v in sorted(numbers.items(), key=lambda x: -x[1])])
    )  # 원소가 많은 순서대로 삽입


# -------------------------------------------------------------------------------------------------------------------------

"""정규식을 이용한 풀이, 원소의 개수가 가장 많은 순서대로 담으면 된다"""
import re
from collections import Counter


def use_re(s):
    s = Counter(re.findall("\d+", s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: -x[1])]))


# --------------------------------------------------------------------------------------------------------------------------

"""test case"""
ss = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}",
]
for s in ss:
    print("나의 풀이: ", solution(s))
    print("답: ", use_re(s))
    print()

# -------------------------------------------------------------------------------------------------------------------------

"""숫자 뽑아내기를 더욱 간편하게"""


def easy(s):
    answer = []

    s1 = s.lstrip("{").rstrip("}").split("},{")

    new_s = []
    for i in s1:
        new_s.append(i.split(","))

    new_s.sort(key=len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


# --------------------------------------------------------------------------------------------------------------------------

"""처음 푼 나의 풀이"""


def s_to_i(s):
    number = []
    flag = False
    tmp = []
    num = ""
    i = 0
    while i < len(s) - 1:
        if s[i] == "}":
            flag = True

        if flag:
            number.append(tmp)
            tmp = []
            flag = False

        if s[i].isdigit():
            num += s[i]
            while s[i + 1].isdigit():
                num += s[i + 1]
                i += 1
            tmp.append(int(num))
            num = ""
        i += 1

    return number


def solution(s):
    answer = []
    numbers = sorted(s_to_i(s), key=lambda x: len(x))

    for number in numbers:
        for num in number:
            if num not in answer:
                answer.append(num)

    return answer
