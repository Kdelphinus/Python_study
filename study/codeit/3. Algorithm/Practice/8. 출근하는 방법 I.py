# 해답을 봄
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
