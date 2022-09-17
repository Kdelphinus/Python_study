def solution(n, m):
    answer = [n, m]
    answer.sort()
    n_tmp = answer[0]
    m_tmp = answer[1]

    if n_tmp == m_tmp:
        return answer

    while n_tmp > 0:  # 유클리드 호제법으로 최대공약수 구하기
        remain = m_tmp % n_tmp
        m_tmp = n_tmp
        n_tmp = remain

    answer[0] = m_tmp
    answer[1] = n * m / m_tmp  # 최대공약수와 최소공배수의 관계

    return answer
