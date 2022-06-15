"""1874 스택 수열"""

import sys

num = int(sys.stdin.readline().rstrip())  # 숫자 개수
stack = []  # 임시 스택
nums = [x for x in range(1, num + 1)]  # 오름차순된 수열
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(num)]  # 만들고 싶은 수열
anw = []  # +와 -가 들어갈 리스트
i = 0  # nums의 인덱스
j = 0  # num_list의 인덱스

while True:
    if not stack or num_list[j] != stack[-1]:  # 스택에 아무것도 없거나 pop할 때가 아니면
        if i == num:  # 근데 이미 nums를 다 돌았다면 종료
            print("NO")
            break
        stack.append(nums[i])
        anw.append("+")
        i += 1
    else:  # 지금 pop 해야 한다면
        anw.append("-")
        stack.pop()
        j += 1

    if j == num:  # num_list를 다 돌았다면
        if not stack:  # 스택이 비었으면 만들고 싶은 수열 완성
            for i in anw:
                print(i)
            break
        else:  # 남았다면 실패
            print("NO")
            break
