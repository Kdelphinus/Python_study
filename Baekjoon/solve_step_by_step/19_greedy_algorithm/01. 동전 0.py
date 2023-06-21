"""11047 동전 0"""

num, value = map(int, input().split())  # 동전 종류와 목표 가치를 받아옴
values = [int(input()) for _ in range(num)]  # 각 동전의 가치를 받아옴
num -= 1  # 인덱스를 맞추기 위해서
cnt = 0  # 횟수를 담을 변수

while value > 0:  # 오름차순으로 돈이 주어지기에 뒤에서부터 가치를 확인한다
    if value >= values[num]:  # 목표 가치 >= 돈의 가치이면 가치만큼 나눠준다
        cnt += value // values[num]
        value %= values[num]
    else:  # 목표 가치 < 돈의 가치면 뺄 수 없기에 한 단계 작은 가치로 이동한다
        num -= 1

print(cnt)
