"""5430 AC"""
import sys
from collections import deque

test = int(sys.stdin.readline())  # 테스트 횟수

for _ in range(test):
    orders = list(sys.stdin.readline().rstrip())  # 명령
    num = int(sys.stdin.readline().rstrip())  # 배열에 들어있는 수의 개수
    input = sys.stdin.readline().rstrip()  # 주어진 배열

    if len(input) < 3:  # 숫자가 없다면
        my_deque = deque()
    else:
        my_deque = deque(input[1:-1].split(","))  # 숫자만 뺴내서 덱으로 만듬

    cnt = 0  # R 명령 횟수를 구할 변수
    check = 0  # error가 떴는지 확인할 변수

    for order in orders:  # 주어진 명령들을 수행
        if order == "R":
            cnt += 1
        elif order == "D":
            if not my_deque:  # 만약 error가 뜨면 에러가 뜬 것을 저장하고 명령 종료
                check += 1
                break

            if cnt % 2 != 0:  # R이 홀수만큼 진행됐으면 R를 한 번 한 것과 같으므로 뒤에것을 뺴줌
                my_deque.pop()
            else:  # R이 짝수만큼 진행됐으면 원래와 동일
                my_deque.popleft()

    if my_deque:  # my_deque가 비어있지 않다면
        print("[", end="")
        if cnt % 2 == 0:  # 총 R 명령이 짝수번이면 순서는 동일
            for i in range(len(my_deque)):
                if i == len(my_deque) - 1:
                    print(f"{my_deque[i]}]")
                else:
                    print(f"{my_deque[i]},", end="")
        elif cnt % 2 != 0:  # 총 R 명령이 홀수번이면 순서는 반대로
            for i in range(len(my_deque) - 1, -1, -1):
                if i == 0:
                    print(f"{my_deque[i]}]")
                else:
                    print(f"{my_deque[i]},", end="")
    else:  # my_deque가 비어있다면
        if check == 0:  # error가 뜨지 않았을 떄
            print("[]")
        else:  # error가 떴을 때
            print("error")
