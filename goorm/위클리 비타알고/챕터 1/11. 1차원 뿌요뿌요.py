# 다섯문제 불통과
num, condition = map(int, input().split())
string = input() + '.'
stack = [string[0]]

cnt = 1
idx = 1
while idx < len(string):
	while stack[-1] == string[idx]:
		idx += 1
		cnt += 1
	
	if cnt >= condition:
		stack.pop()
	else:
		tmp = stack[-1]
		for _ in range(1, cnt):
			stack.append(tmp)
	
	if stack and stack[-1] == string[idx]:
		cnt = 2
	else:
		stack.append(string[idx])
		cnt = 1
	idx += 1

stack.pop()
if not stack:
	print("CLEAR!")
else:
	for s in stack:
		print(s, end="")

# -----------------------------------------------------------------------

# 시간 초과
#num, condition = map(int, input().split())
#string = input()

#while True:
#    cnt = 1
#    idx = 1
#    char = string[0]
#    change = []
#    while idx < len(string):
#        while idx < len(string) and char == string[idx]:
#            cnt += 1
#            idx += 1
        
#        if cnt >= condition:
#            change.append(char * cnt)
        
#        if idx < len(string):
#            char = string[idx]
#            idx += 1

#    if not change:
#        print(string)
#        break

#    for c in change:
#        string = string.replace(c, "")

#    if string == "":
#        print("CLEAR!")
#        break