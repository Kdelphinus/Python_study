"""월간 코드 챌린지 시즌 1"""


def solution(n):
    answer = 0
    num = ""
    while n > 0:  # 0이 될때까지 3으로 나눔
        num += str(n % 3)  # 나머지를 저장하면 뒤집은 3진법과 동일
        n //= 3

    power = 0  # 지수
    for i in range(len(num) - 1, -1, -1):  # 뒤에서부터 확인
        tmp = int(num[i])  # 숫자를 꺼내고
        answer += tmp * (3 ** power)  # 3진법에서 10진법으로 변환
        power += 1

    return answer


print(solution(45))
print(solution(125))
