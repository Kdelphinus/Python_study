number = input()
flag = False

# 12를 먼저 찾는 경우
one_two = number.replace("12", "00", 1)
if one_two != number:
	one_two_one = one_two.replace("21", "00", 1)
	if one_two_one != one_two:
		flag = True

# 21을 먼저 찾는 경우
two_one = number.replace("21", "00", 1)
if two_one != number:
	two_one_two = two_one.replace("12", "00", 1)
	if two_one_two != two_one:
		flag = True
		
if flag:
	print("Yes")
else:
	print("No")