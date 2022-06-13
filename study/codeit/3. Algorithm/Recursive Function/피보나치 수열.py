def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# 테스트: fib(1)부터 fib(10)까지 출력
print(fib(50))