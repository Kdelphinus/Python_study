"""2018 KAKAO BLIND RECRUITMENT"""
comp = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def solution(msg):
    """LZW 압축을 구현한 함수"""
    answer = []
    end_num = 27  # 새로 추가할 사전의 번호
    idx = 0  # 문자열 인덱스
    while True:
        i = 1  # 끝나는 인덱스
        while True:  # 사전에 있는 단어인지 확인
            if idx + i + 1 > len(msg) or msg[idx : idx + i + 1] not in comp:
                break
            i += 1

        if idx + i == len(msg):  # 마지막 단어일 때
            if msg[idx : idx + i] in comp:  # 있으면 사전에 저장된 번호로
                answer.append(comp[msg[idx : idx + i]])
            else:  # 없으면 새로 추가할 번호를 바로 삽입
                answer.append(end_num)
            return answer

        answer.append(comp[msg[idx : idx + i]])  # 압축된 번호 입력
        comp[msg[idx : idx + i + 1]] = end_num  # 새로운 단어는 사전에 저장
        end_num += 1  # 다음 저장할 번호
        idx += i  # 다음 탐색할 시작 인덱스


print(solution("KAKAO"))  # [11, 1, 27, 15]
print(solution("DELPHINUS"))  # [4, 5, 12, 16, 8, 9, 14, 21, 19]

# ------------------------------------------------------------------------------------------------------

"""같은 원리, 간단한 구현"""


def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[: tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
