test = int(input())
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for t in range(test):
	tmp = ''
	string = input()
	for s in string:
		if s in vowel:
			tmp += s
	
	if tmp:
		print(tmp)
	else:
		print('???')