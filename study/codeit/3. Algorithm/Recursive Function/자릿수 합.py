# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    num = len(str(n))
    if num <= 1:
        return n
    sum = n // 10**(num - 1)
    i = sum * 10**(num - 1)
    return sum_digits(n-i) + sum


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))


# 모범답안
# def sum_digits(n):
#     if n < 10:
#         return n
#     return n % 10 + sum_digits(n // 10)