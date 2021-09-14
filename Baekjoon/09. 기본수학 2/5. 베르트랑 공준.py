""" 4948 베르트랑 공준 (두 자연수 사이에는 최소 1개 이상의 소수가 있다) """


def isPrime(num):
    if num <= 1:
        return False

    i = 2
    while i * i <= num:  # 제곱근까지만 계산, 2와 3은 바로 True
        if num % i == 0:
            return False
        i += 1
    return True


# 상한수(여기선 123,456)까지 리스트를 미리 만들어 소수 여부를 먼저 판단
num_lsit = list(range(2, 246912))  # 123456 * 2 = 246912
prime_list = []
for i in num_lsit:
    if isPrime(i):
        prime_list.append(i)

while True:
    num = int(input())
    if num == 1:
        print(num)
    elif num == 0:
        break
    else:
        cnt = 0
        for i in prime_list:
            if num < i < 2 * num + 1:
                cnt += 1
        print(cnt)

# ----------------------------------------------------------------------------------

"""밑의 코드처럼 소수 여부를 먼저 판단하지 않으면 시간초과"""
# def isPrime(num):
#     if num <= 1:
#         return False

#     i = 2
#     while i * i <= num:  # 제곱근까지만 계산, 2와 3은 바로 True
#         if num % i == 0:
#             return False
#         i += 1
#     return True


# while True:
#     num = int(input())
#     cnt = 0

#     if num == 0:
#         break

#     for i in range(num + 1, 2 * num + 1):
#         if isPrime(i):
#             cnt += 1

#     print(cnt)
