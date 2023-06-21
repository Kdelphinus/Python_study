""" 9020 골드바흐의 추측 """
""" 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 추측
앞서 푼 것들을 이용하면 시간초과에 걸리므로 소수 찾기부터 에라토스테네스의 체로 변경 """


def prime_list(n):
    num = [True] * n

    for i in range(2, int(n**0.5) + 1):  # 소수는 제곱근까지만 나눠보면 알 수 있음
        if num[i] == True:
            for j in range(i + i, n, i):  # i 이후, i의 배수들은 모두 False
                num[j] = False

    return num


T = int(input())

for i in range(T):
    num = int(input())
    anw = prime_list(num)

    for j in range(num // 2, 1, -1):  # 절반 지점, 큰 수부터 확인
        if anw[j] == True and anw[num - j] == True:
            print(j, num - j)
            break
