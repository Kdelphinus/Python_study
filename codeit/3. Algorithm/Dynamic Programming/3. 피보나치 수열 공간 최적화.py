def fib_optimized(n):
    current = 1
    previous = 1
    if n <= 2:
        return 1
    else:
        for i in range(3, n + 1):
            tem = current
            current = current + previous
            previous = tem
        return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

# -------------------------------------------------------------------------------------

# 답안
def fib_optimized(n):
    current = 1
    previous = 0

    # 반복적으로 위 변수들을 업데이트한다.
    for i in range(1, n):
        current, previous = current + previous, current

    # n번재 피보나치 수를 리턴한다.
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))