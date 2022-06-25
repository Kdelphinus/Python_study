"""9375 패션왕 신해빈"""

test = int(input())

for _ in range(test):
    num = int(input())  # 가진 의상의 수
    kinds = {}  # 의상 종류가 들어감

    for i in range(num):
        custume, kind = map(str, input().split())

        if kind in kinds:  # 이미 사전에 있으면 개수만 추가해준다
            kinds[kind] += 1
        else:  # 사전에 없으면 만들어준다
            kinds[kind] = 1

    values = list(kinds.values())  # 종류 별 옷의 개수만 받아서 리스트로 만든다
    value = 1
    for j in values:  # 경우의 수 구하기(안 입는 것까지 구하기 위하여 1을 더함)
        value *= j + 1
    print(value - 1)  # 다 벗는 것을 제외하기 위하여 1을 뺌
