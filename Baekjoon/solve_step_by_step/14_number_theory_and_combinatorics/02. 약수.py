"""1037 약수"""

num = int(input())  # 약수의 개수
factor = sorted(list(map(int, input().split())))  # 약수가 담긴 리스트를 오름차순

print(factor[0] * factor[-1])  # 맨 앞의 수와 맨 뒤의 수의 곱을 출력
