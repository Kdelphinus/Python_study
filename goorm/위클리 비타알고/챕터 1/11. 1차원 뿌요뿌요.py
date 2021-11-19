# stack 활용
num, condition = map(int, input().split())
string = input()
stack = []
idx = 0
while idx < len(string):
    # 스택이 비어있거나 앞 문자와 같지 않으면 스택에 삽입
    if not stack or stack[-1][0] != string[idx]:
        stack.append([string[idx], 1])  # [문자, 반복된 횟수]
        idx += 1

    # 앞 문자와 다를 때까지 한 칸씩 탐색하며 문자가 반복된 횟수를 늘린다
    while idx < len(string) and stack[-1][0] == string[idx]:
        idx += 1
        stack[-1][1] += 1

    # 반복된 횟수가 조건에 부합하면 빼준다
    if stack and stack[-1][1] >= condition:
        stack.pop()

if not stack:  # 스택이 비었다면 클리어
    print("CLEAR!")
else:  # 남아있다면 남은 것을 출력
    for s, cnt in stack:
        for c in range(cnt):
            print(s, end="")

# -----------------------------------------------------------------------

# 시간 초과
# num, condition = map(int, input().split())
# string = input()

# while True:
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
