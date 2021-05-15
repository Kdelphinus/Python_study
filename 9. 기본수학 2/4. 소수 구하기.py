""" 1929 소수 구하기 """

m, n = map(int, input().split())


def isPrime(num):
    if num <= 1:
        return False

    i = 2
    while i * i <= num:  # 제곱근까지만 계산, 2와 3은 바로 True
        if num % i == 0:
            return False
        i += 1
    return True


for i in range(m, n + 1):
    if isPrime(i):  # isPrime(i)가 True일 때만 출력
        print(i)
