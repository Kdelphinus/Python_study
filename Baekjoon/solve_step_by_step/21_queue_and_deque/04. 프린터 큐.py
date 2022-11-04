"""1966 프린터 큐"""
import sys
from collections import deque

test = int(sys.stdin.readline())  # 테스트 횟수

for _ in range(test):
    num, index = map(int, sys.stdin.readline().split())  # num개의 문서 중 index번째 문서에 대하여
    importance = list(map(int, sys.stdin.readline().split()))  # 중요도를 받음
    impor_sort = sorted(importance)  # 중요도 순으로 내림차순한 리스트
    importance = deque(importance)  # queue로 변환
    cnt = 1  # 몇 번째로 뽑을지 저장하는 변수

    while True:
        if importance[0] == impor_sort[-1]:  # 맨 앞에 있는 문서가 중요도가 가장 높을 때
            if index == 0:  # 그 문서가 우리가 원하는 문서면
                print(cnt)
                break
            else:  # 원하는 문서가 아니면
                importance.popleft()  # 가장 중요한 것을 하나 버리고
                impor_sort.pop()  # 뽑은 문서도 버리고
                cnt += 1  # 인쇄 횟수 1 추가
                index -= 1  # 문서를 앞으로 한 칸 이동
        else:  # 맨 앞에 있는 문서를 뽑을 때가 아니면
            importance.append(importance.popleft())  # 맨 앞에 있는 문서를 맨 뒤로 이동
            if index == 0:  # 옮긴 문서가 우리가 원하는 문서이면
                index = len(importance) - 1  # 인덱스를 문서 끝으로 이동
            else:  # 옮긴 문서가 우리가 원하는 문서가 아니면
                index -= 1  # 문서를 앞으로 한 칸 이동
