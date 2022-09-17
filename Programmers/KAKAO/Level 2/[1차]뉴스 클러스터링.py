"""2018 KAKAO BLIND RECRUITMENT"""

"""나의 풀이"""


def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()  # 소문자로 변경
    string1 = []
    string2 = []
    tmp = ""

    for i in str1:
        if i.isalpha():  # 문자이면
            tmp += i  # 임시로 저장하고
            if len(tmp) == 2:  # 만약 두 글자면
                string1.append(tmp)  # 배열에 추가하고
                tmp = i  # 나중에 들어온 문자만 남긴다
        else:  # 문자가 아니면
            tmp = ""  # 임시 문자열 초기화
    tmp = ""
    for i in str2:  # str1과 동일한 구동방식
        if i.isalpha():
            tmp += i
            if len(tmp) == 2:
                string2.append(tmp)
                tmp = i
        else:
            tmp = ""

    if not string1 and not string2:  # 두 배열이 모두 공집합이면
        return 65536  # 1이기에 65536을 곱하여 리턴

    check = []  # 확인한 문자열을 보관하는 리스트
    total = 0  # 합집합의 길이
    union = 0  # 교집합의 길이
    for i in string1:
        if i in string2 and i not in check:  # string2에도 들어있으면서 아직 확인하지 않은 문자열
            check.append(i)  # 확인했다고 표시
            i_num1 = string1.count(i)  # string1에 들어있는 개수
            i_num2 = string2.count(i)  # string2에 들어있는 개수
            total += max(i_num1, i_num2)  # 더 많은 것을 합집합 개수에 추가
            union += min(i_num1, i_num2)  # 더 적은 것을 교집합 개수에 추가
        elif i not in string2:  # 만약 string2엔 없다면
            total += 1  # 합집합 개수에만 추가
    for i in string2:
        if i not in string1:  # 교집합은 이미 구했기에 합집합만 구함
            total += 1

    return int(union / total * 65536)  # 계산 후, 소수점자리는 버림


# ---------------------------------------------------------------------------------------------------------

"""최다 추천 풀이"""
import re
import math


def solution(str1, str2):
    # 문자열로 구성된 단어만 str 리스트에 저장
    str1 = [
        str1[i : i + 2].lower()
        for i in range(0, len(str1) - 1)
        if not re.findall("[^a-zA-Z]+", str1[i : i + 2])
    ]
    str2 = [
        str2[i : i + 2].lower()
        for i in range(0, len(str2) - 1)
        if not re.findall("[^a-zA-Z]+", str2[i : i + 2])
    ]

    gyo = set(str1) & set(str2)  # 교집합에 들어있는 원소
    hap = set(str1) | set(str2)  # 합집합에 들어있는 원소

    if len(hap) == 0:
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])  # 교집합의 개수
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])  # 합집합의 개수

    return math.floor((gyo_sum / hap_sum) * 65536)
