a, b = map(int, input().split())
if a != b: # a와 b가 다르다면 그 사이 수의 약수들의 개수는 무조건 2가 가장 많다
	print(2)
else: # a == b일 때
	for i in range(2, int(b ** 0.5) + 1):
		if b % i == 0: # 약수를 찾으면 출력 후 종료(다 한 개이므로 가장 작은 것을 출력)
			print(i)
			break
	else: # break가 실행되지 않았다면 소수이므로 자신을 출력
		print(b)