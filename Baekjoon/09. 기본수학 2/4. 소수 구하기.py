""" 1929 소수 구하기 """


def prime_list(n):
    """에라토스테네스의 체로 소수를 구하는 함수"""
    prime_number = [True] * (n + 1)
    prime_number[1] = False

    for i in range(2, int(n ** 0.5) + 2):
        if prime_number[i]:
            for j in range(i + i, n + 1, i):
                prime_number[j] = False

    return prime_number


m, n = map(int, input().split())
prime_number = prime_list(n)
for i in range(m, n + 1):
    if prime_number[i]:
        print(i)
