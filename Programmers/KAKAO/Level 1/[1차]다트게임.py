"""2018 KAKAO BLIND RECRUITMENT"""


def solution(dartResult):
    dartResult += "0"  # 마지막 점수도 추가되도록 마지막에 숫자 추가
    answer = []
    i = 1

    tmp = ""
    tmp += dartResult[0]  # 처음은 숫자이므로 추가
    if dartResult[1].isdigit():  # 만약 두자리수라면
        tmp += dartResult[1]  # 뒤에도 추가
        i += 1  # 인덱스 하나 추가

    while i < len(dartResult):
        if dartResult[i].isdigit():  # 현재 위치가 숫자라면
            j = 0
            while j < len(tmp):  # 지금까지 저장한 결과를 확인
                if j:
                    if tmp[j].isalpha():  # SDT 중 하나일 때
                        if tmp[j] == "D":
                            answer[-1] = answer[-1] ** 2
                        elif tmp[j] == "T":
                            answer[-1] = answer[-1] ** 3
                    else:  # *, # 일때
                        if tmp[j] == "*":
                            answer[-1] *= 2
                            if len(answer) > 1:
                                answer[-2] *= 2
                        else:
                            answer[-1] *= -1
                else:  # 결과의 첫번째는 점수
                    if tmp[j + 1].isdigit():  # 만약 두자릿수라면
                        answer.append(int(tmp[j] + tmp[j + 1]))
                        j += 1
                    else:
                        answer.append(int(tmp[j]))
                j += 1
            tmp = dartResult[i]  # 이전에 저장한 결과 점수 계산이 끝나면 새로운 점수로 변경
            if i < len(dartResult) - 1 and dartResult[i + 1].isdigit():  # 두자릿수면 뒤에도 추가
                tmp += dartResult[i + 1]
                i += 1

        else:  # 숫자가 아니면 저장
            tmp += dartResult[i]
        i += 1
    return sum(answer)


# -----------------------------------------------------------------------------------------
# 비슷한 풀이, 더 간단한 구현


def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace("10", "k")  # 10을 k로 바꿔 한자리 글자로 만듬
    point = ["10" if i == "k" else i for i in dartResult]  # 그 후, k를 10이라는 하나의 글자로 다시 추가
    # print(point) # 확인용

    i = -1
    sdt = ["S", "D", "T"]
    for j in point:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j) + 1)
        elif j == "*":
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i - 1] = answer[i - 1] * 2
        elif j == "#":
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
