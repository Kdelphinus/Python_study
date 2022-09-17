def solution(n):
    answer = 0

    for i in range(2, n + 1):
        flag = True
        for j in range(2, int(i ** 0.5) + 1):  # 제곱근까지만 확인
            if i % j == 0:  # 나눠지는게 있으면 소수가 아님
                flag = False
                break
        if flag:  # 나눠지는게 하나도 없었다면 소수
            answer += 1

    return answer


# 에라토스테네스의 체 사용
def solution(n):
    num = set(range(2, n + 1))  # 확인할 숫자들을 set으로 만듬

    for i in range(2, n + 1):
        if i in num:  # set에 숫자가 있다면
            num -= set(range(2 * i, n + 1, i))  # 그 숫자의 배수들은 모두 지운다
    return len(num)
