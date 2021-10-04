"""1644 소수의 연속합"""


def __Eratos(num):
    """__Eratos 에라토스테네스의 체

    Args:
        num (int): 1 ~ num의 수

    Returns:
        prime_number (list): 1 ~ num 사이의 소수를 가지는 리스트
    """
    prime_number = []
    numbers = [True] * (num + 1)
    numbers[0] = False
    numbers[1] = False

    for i in range(2, num + 1):
        if numbers[i]:
            prime_number.append(i)
            for j in range(i * 2, num + 1, i):
                numbers[j] = False
    return prime_number


def two_pointer(goal):
    prime_number = __Eratos(goal)  # 1 ~ goal 사이의 소수들을 가진 리스트
    tmp = 0  # 부분합
    end = 0
    cnt = 0

    for start in range(len(prime_number)):
        while end < len(prime_number) and tmp < goal:
            tmp += prime_number[end]
            end += 1

        if tmp == goal:
            cnt += 1
        tmp -= prime_number[start]

    return cnt


goal = int(input())
print(two_pointer(goal))
