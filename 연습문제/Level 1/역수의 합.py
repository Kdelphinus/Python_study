def solution(n):
    answer = 0

    for i in range(1, int(n ** 0.5) + 1):  # 제곱근까지 확인
        if n % i == 0:  # 나누어진다면
            answer += i  # 값을 더하고
            if n // i != i:  # 몫과 값이 같지 않다면(즉 제곱근이 아니면)
                answer += n // i  # 몫도 더한다
    return answer
