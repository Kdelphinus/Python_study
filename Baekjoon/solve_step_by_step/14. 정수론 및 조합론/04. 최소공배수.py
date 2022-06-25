"""1934 최소공배수"""
"""이미 03번에서 효율적인 방법을 썼기에 코드의 차이가 거의 없음"""
test = int(input())

for _ in range(test):
    x, y = sorted(map(int, input().split()))  # 두 숫자를 받는다 (x <= y)

    # 원래 값을 보존하기 위해
    x_tem = x
    y_tem = y

    if x == y:
        print(x)
    else:
        while True:  # 유클리드 호제법으로 최대공약수 구하기
            remain = y_tem % x_tem
            y_tem = x_tem
            x_tem = remain

            # 유클리드 호제법을 확인할 테스트 코드
            # print(y_tem, x_tem)

            if x_tem == 0:
                break

        print(int(abs(x * y) / y_tem))  # 최소공배수와 최대공약수의 관계를 이용


# -----------------------------------------------------------------------------------
# 다른 답안, 위의 코드를 재귀로 구현
def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    return a * b // gcd(a, b)


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))