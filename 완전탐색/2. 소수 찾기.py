# """나의 풀이"""
# from itertools import permutations


# def is_prime(num):
#     """소수인지 판단하는 함수"""

#     if num <= 1:  # 1 이하는 소수 아님
#         return False

#     i = 2
#     while i * i <= num:  # 제곱근까지만 구하면 소수 판정 가능
#         if num % i == 0:
#             return False
#         i += 1

#     return True


# def solution(num):
#     """주어진 숫자 문자열을 조합하여 만들 수 있는 소수의 개수를 구하는 함수"""
#     answer = 0
#     str_numbers = []
#     for i in range(1, len(num) + 1):  # 주어진 숫자들을 이용하여 만들 수 있는 모든 숫자
#         str_numbers += list(map("".join, permutations(num, i)))

#     numbers = []
#     for number in str_numbers:
#         number = int(number)
#         if number not in numbers:  # 구한 문자열 숫자를 정수형으로 바꾸고 중복되지 않는 숫자만 구함
#             numbers.append(number)
#             if is_prime(number):  # 소수일 때 개수 추가
#                 answer += 1

#     return answer, len(numbers)


# print(solution("175"))  # 1, 7, 5의 조합으로 만들 수 있는 소수의 수

# ---------------------------------------------------------------------------------------------------------
"""다른 답안"""

from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(
            map(int, map("".join, permutations(list(n), i + 1)))
        )  # set은 +연산은 안되나 |(bit 연산)은 가능
    a -= set(range(0, 2))  # 0, 1 제거
    for i in range(2, int(max(a) ** 0.5) + 1):  # 에라토스테네스 체
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


print(solution("17"))