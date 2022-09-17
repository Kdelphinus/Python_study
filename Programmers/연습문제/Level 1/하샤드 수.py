def solution(x):
    tmp = x
    num = 0

    while tmp > 0:
        num += tmp % 10
        tmp //= 10
    if x % num:
        return False
    return True
