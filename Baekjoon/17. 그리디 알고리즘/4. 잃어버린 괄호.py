"""1541 잃어버린 괄호"""

eq_str = input()  # 식을 받음
plus = []  # 양수가 될 숫자들
minus = []  # 음수가 될 숫자들
start = 0  # 숫자 인덱스 시작 부분
negative = False  # - 기호가 나왔는가

for i in range(len(eq_str)):
    if negative:  # 마이너스 기호가 나왔다면
        if eq_str[i] == "+" or eq_str[i] == "-":
            minus.append(int(eq_str[start:i]))
            start = i + 1
        if i == len(eq_str) - 1:  # 마지막 숫자라면
            minus.append(int(eq_str[start:]))
    else:
        if eq_str[i] == "+":
            plus.append(int(eq_str[start:i]))
            start = i + 1
        elif eq_str[i] == "-":
            plus.append(int(eq_str[start:i]))
            start = i + 1
            negative = True
        if i == len(eq_str) - 1:  # 마지막 숫자라면
            plus.append(int(eq_str[start:]))

print(sum(plus) - sum(minus))


# ----------------------------------------------------------------------------------------
# 다른 답안(시간은 거의 비슷)
a = input().split("-")  # - 부호를 기준으로 나눔
num = []
for i in a:
    cnt = 0
    s = i.split("+")
    for j in s:  # 나눠진 식들을 다시 + 부호로 나누어 더해준다
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
print(num)
print(a)