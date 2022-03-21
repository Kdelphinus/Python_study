"""2022 KAKAO BLIND RECRUITMENT"""


def convert(num, base):
    """
    원하는 진수로 변환 하는 함수
    Args:
        num: 변환할 수
        base: 변환할 진수

    Returns: 변환된 수

    """
    q, r = divmod(num, base)
    if q:
        return convert(q, base) + str(r)
    else:
        return str(r)


def create_prime_number(num):
    """에라토스테네스의 체를 반환하는 함수"""
    prime_number = [True] * (num + 1)
    prime_number[1] = False
    for i in range(2, int(num ** 0.5) + 2):
        if prime_number[i]:
            for j in range(i * 2, num + 1, i):
                prime_number[j] = False

    return prime_number


def isPrime(num):
    """num이 소수인지 판별하는 함수"""
    for i in range(3, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    numbers = convert(n, k).replace("0", " ").split()
    prime_number = create_prime_number(n)
    for number in numbers:
        if int(number) < len(prime_number):
            if prime_number[int(number)]:
                answer += 1
        else:  # 에라토스테네스의 체를 벗어나면 직접 소수 판별
            if isPrime(int(number)):
                answer += 1


print(solution(1, 3))
