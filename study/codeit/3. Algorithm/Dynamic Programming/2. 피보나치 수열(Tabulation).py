def fib_tab(n):
    fib_cache = []
    i = 0
    while len(fib_cache) != n:
        if i < 2:
            fib_cache.append(1)
        elif i >= 2:
            fib_cache.append(fib_cache[i - 1] + fib_cache[i - 2])
        i += 1
    return fib_cache[n - 1]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))


# 답안
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))