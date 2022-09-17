"""2018 KAKAO BLIND RECRUITMENT"""
import string


def solution(n, t, m, p):
    """solution

    Args:
        n (int): n진수의 n
        t (int): 미리 구할 숫자의 개수
        m (int): 게임에 참가하는 인원
        p (int): 내가 참여한 게임의 순서

    Returns:
        answer (str): 말해야 하는 숫자 t개를 공백없이 문자열로 출력
    """
    temp = string.digits + string.ascii_uppercase

    def convert(num, base):
        q, r = divmod(num, base)
        if q:
            return convert(q, base) + temp[r]
        return temp[r]

    num = 0
    number = ""
    while len(number) < t * m:
        number += convert(num, n)
        num += 1

    idx = p - 1
    answer = ""
    while True:
        answer += number[idx]
        idx += m
        if len(answer) == t:
            return answer
