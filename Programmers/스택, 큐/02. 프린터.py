from collections import deque


def solution(priorities, location):
    if len(priorities) == 1:  # 작업 목록이 하나면 바로 뽑고 종료
        return 1

    priorities = deque(priorities)
    answer = 0  # 몇 번째로 뽑히는지 저장할 변수

    while True:
        temp_list = max(list(priorities)[1:])  # 현재 작업 문서를 제외한 나머지 문서들 중 최대값

        if priorities[0] >= temp_list:  # 가장 앞에 있는 문서를 뽑아야 할 때
            priorities.popleft()  # 가장 앞 문서를 뽑고
            answer += 1  # 뽑은 횟수 추가

            if location == 0:  # 지금 뽑은 문서가 알고 싶은 문서일 때
                return answer
            elif len(priorities) == 1:  # 남은 문서가 하나만 남았을 때
                return answer + 1
            else:
                location -= 1
        else:  # 가장 앞에 있는 문서가 지금 뽑을 때가 아닐 때
            temp = priorities.popleft()
            priorities.append(temp)

            if location == 0:  # 가장 앞에 있는 문서가 알고 싶은 문서일 때
                location = len(priorities) - 1
            else:
                location -= 1


priorities = [2, 1, 3, 2]  # 중요도
print(solution(priorities, 2))