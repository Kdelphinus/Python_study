"""5086 배수와 약수"""

while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0: # 종결조건
        break

    if x > y and x % y == 0: # x가 y의 배수일 조건
        print("multiple")
    elif x < y and y % x == 0: # x가 y의 약수일 조건
        print("factor")
    else: # 둘 다 아닐 때
        print("neither")
