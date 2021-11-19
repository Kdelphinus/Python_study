# 전반적으로 스택의 괄호 문제와 유사
# 같은 풀이, 다른 문제도 풀이방법을 찾도록 연습하기
num = int(input())
stack = []
hw = []

# 과제날짜를 수로 변환하여 저장(ex. 10/15 -> 1015, 3/1 -> 301)
for i in range(1, num + 1):
	start, end = input().split()
	start = list(map(int, start.split('/')))
	end = list(map(int, end.split('/')))
	hw.append([start[0] * 100 + start[1], end[0] * 100 + end[1]])
	
hw.sort(key=lambda x: (x[0], -x[1])) # 시작 날짜는 오름차순, 마감 날짜는 내림차순으로 정렬
hw_sorted = [] # 과제 날짜 별로 정렬할 리스트
for idx, h in enumerate(hw):
	hw_sorted.append([h[0], idx + 1]) # 시작 날짜는 인덱스를 양수로 저장
	hw_sorted.append([h[1], -(idx + 1)]) # 마감 날짜는 인덱스를 음수로 저장
hw_sorted.sort() # 날짜별로 정렬

for h in hw_sorted:
	if h[1] > 0: # 시작 날짜면
		stack.append(h) # 스택에 추가
	else: # 마감 날짜면
        # 이때 스택이 비었거나 하고 있는 과제가 마감해야하는 과제와 다르다면
		if len(stack) == 0 or -stack[-1][1] != h[1]:
			print("No") # 과제를 모두 마칠 수 없다
			break
		stack.pop() # 마감해야 하는 과제와 하고 있는 과제가 같으면 제출
else: # 모든 과제를 제출할 수 있다
	print("Yes")
	