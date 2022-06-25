"""2609 최대공약수와 최소공배수"""
x, y = sorted(map(int, input().split()))  # 두 숫자를 받는다 (x <= y)

# 원래 값을 보존하기 위해
x_tem = x
y_tem = y

if x == y:
    print(x)
    print(x)
else:
    while True:  # 유클리드 호제법으로 최대공약수 구하기
        remain = y_tem % x_tem
        y_tem = x_tem
        x_tem = remain

        # 유클리드 호제법을 확인할 테스트 코드
        # print(y_tem, x_tem)

        if x_tem == 0:
            print(y_tem)
            break

    print(int(abs(x * y) / y_tem))  # 최소공배수와 최대공약수의 관계를 이용
