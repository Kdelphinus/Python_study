"""2004 조합 0의 개수"""

# 11번 문제에서 팩토리얼을 이항 계수로 바꾼 것
# 이항계수 정의를 직접 이용하면 시간초과가 나온다
# from math import factorial

# num, k = map(int, input().split())
# value = str(factorial(num) // (factorial(num - k) * factorial(k)))  # 조합 값을 문자열로 바꾼다
# length = len(value)
# i = -1  # 뒤에서부터 보기때문에 인덱스를 -1부터 작아지는 방향으로 간다
# cnt = 0  # 횟수를 저장하는 변수

# while i >= -length:
#     if value[i] == "0":  # 0이면 횟수 추가, 인덱스 이동
#         cnt += 1
#         i -= 1
#     else:  # 0이 아니면 반복문 바로 종료
#         break

# print(cnt)


# --------------------------------------------------------------------------------------------------------
"""0은 2와 5(2 x 5 = 10)이 만들어낸다.
그렇기에 factorial(num)이 가진 2의 개수 - factorial(num - k)이 가진 2의 개수 - factorial(k)이 가진 2의 개수와
factorial(num)이 가진 5의 개수 - factorial(num - k)이 가진 5의 개수 - factorial(k)이 가진 5의 개수 중 작은 값과 같다"""


def num_count(num, div):
    # num: div를 포함한 숫자, div: factorial(num)에 얼마나 포함됐는지 구할 숫자
    cnt = 0
    while num > 0:
        num //= div
        cnt += num
    return cnt


num, k = map(int, input().split())

num_five_cnt = (
    num_count(num, 5) - num_count(k, 5) - num_count(num - k, 5)
)  # num C K가 가진 5의 개수
num_two_cnt = (
    num_count(num, 2) - num_count(k, 2) - num_count(num - k, 2)
)  # num C K가 가진 2의 개수

print(min(num_two_cnt, num_five_cnt))