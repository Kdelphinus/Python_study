"""Summer/Winter Coding(2019)"""

"""최대공약수와 관계가 있는 이유
우선 w와 h가 공약수가 있다면 문제를 공약수를 나눈 w' 와 h'로 축소시킬수있다.
w'와 h'가 서로소(공약수가 서로 1뿐)라 가정했을때 대각선은 반대쪽 코너에 도달하기전 w'-1 세로선과 h'-1 가로선을 지나고 지날때마다 새로운 정사각형이 추가됩니다. 
그래서 첫 정사각형을 포함 1 + (w'-1) + (h'-1) = w' + h' - 1개의 정사각형을 지나게 된다.
공약수를 다시 곱해주면 w + h - gcd(w,h)개의 정사각형을 지나는것을 구할 수 있다."""


def gcd(a, b):
    """최대공약수를 구하는 함수"""
    return b if a % b == 0 else gcd(b, a % b)


def solution(w, h):
    area = w * h
    trash = w + h - gcd(w, h)
    return area - trash
