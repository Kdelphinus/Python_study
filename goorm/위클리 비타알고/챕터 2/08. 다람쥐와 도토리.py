MOD = 1000000007


def fpow(a, n):
    ret = 1

    while n:
        if n % 1:
            ret = ret * a % MOD
        a = a * a % MOD


# ==========================================================================================

""" 페르마의 소정리(백준 20 - 5 참고)
정수 a와 a의 배수가 아니면서 소수(prime number)인 p는 다음 식을 성립한다
-> (a ** p) % p = a % p

위 식을 토대로 밑의 식도 유추할 수 있다
-> (a ** (p - 1)) % p = 1 % p
-> (a ** (p - 2)) % p = (a ** (-1)) % p = (1 / a) % p"""

# P = 1000000007


# def power(number, num):
#    """power 빠른 제곱법

#    Args:
#        number (int): 수
#        num (int): 지수

#    Returns:
#        (int): number^num
#    """
#    if num == 0:  # 제곱수가 1일 때
#        return 1
#    else:
#        if num % 2 == 0:  # 제곱수가 짝수일 때
#            return (power(number, num // 2) ** 2) % P
#        else:  # 제곱수가 홀수일 때
#            return (power(number, num // 2) ** 2 * number) % P


# def binomial_coefficient(n, r):
#    """binomial_coefficient 페르마 소정리와 빠른 제곱법을 이용하여 이항계수 계산

#    Args:
#        n (int): n_C_r 중 n
#        r (int): n_C_r 중 r

#    Returns:
#        (int): n_C_r의 값
#    """
#    numerator = fact[n]
#    denominator = (fact[r] * fact[n - r]) % P

#    """ 답을 구하는 식이 나오는 과정
#    (numerator * (denominator ** -1)) % p = (numerator * ((denominator ** (p-2)) % p)) % p"""
#    return (numerator * (power(denominator, P - 2)) % P) % P


# width, height = map(int, input().split())
# target_x, target_y = map(int, input().split())
# trap_x, trap_y = map(int, input().split())

## FIXME
## factorial 부분에서 runtimeerror 발생
# fact = [1 for _ in range(width + height + 1)]
# for i in range(2, width + height + 1):
#    fact[i] = fact[i - 1] * i % P

# if target_x >= trap_x and target_y >= trap_y:  # 도토리 주우러 가는 길에 함정이 있을 때
#    # 출발위치에서 도토리까지 가는 최단 경로의 수
#    to_target_all = binomial_coefficient(target_x + target_y, target_x)
#    # 출발위치에서 함정까지 가는 최단 경로의 수
#    to_start_trap = binomial_coefficient(trap_x + trap_y, trap_x)
#    # 함정에서 도토리까지 가는 최단 경로의 수
#    to_trap_target = binomial_coefficient(
#        target_x + target_y - trap_x - trap_y, target_x - trap_x
#    )

#    # 출발위치에서 도토리까지 함정을 피해 가는 최단 경로의 수
#    to_target = to_target_all - (to_start_trap * to_trap_target) % P

#    # 도토리에서 출구로 가는 최단 경로의 수
#    to_exit = binomial_coefficient(
#        width + height - target_x - target_y, width - target_x
#    )
# elif target_x <= trap_x and target_y <= trap_y:  # 출구로 가는 길에 함정이 있을 때
#    # 출발위치에서 도토리까지 가는 최단 경로의 수
#    to_target = binomial_coefficient(target_x + target_y, target_x)

#    # 도토리에서 출구까지 가는 최단 경로의 수
#    to_exit_all = binomial_coefficient(
#        width + height - target_x - target_y, width - target_x
#    )
#    # 도토리에서 함정까지 가는 최단 경로의 수
#    to_target_trap = binomial_coefficient(
#        trap_x + trap_y - target_x - target_y, trap_x - target_x
#    )
#    # 함정에서 출구까지 가는 최단 경로의 수
#    to_trap_exit = binomial_coefficient(
#        width + height - trap_x - trap_y, width - trap_x
#    )

#    # 도토리에서 출구까지 함정을 피해 가는 최단 경로의 수
#    to_exit = to_exit_all - (to_target_trap * to_trap_exit) % P
# else:  # 최단 거리에 함정이 없는 경우
#    # 출발위치에서 도토리까지 최단 경로의 수
#    to_target = binomial_coefficient(target_x + target_y, target_x)

#    # 도토리에서 출구까지 최단 경로의 수
#    to_exit = binomial_coefficient(
#        width + height - target_x - target_y, width - target_x
#    )

# print(to_exit * to_target % P)
