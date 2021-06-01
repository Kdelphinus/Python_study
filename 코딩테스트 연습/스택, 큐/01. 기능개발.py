from collections import deque


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []  # 배포할 때 몇 개의 기능이 배포되는지 담을 리스트
    cnt = 0  # 배포될 기능을 세는 변수

    while True:
        for i in range(len(progresses)):  # 작업 진행
            progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] >= 100:  # 최우선 기능부터 작업이 완료되었나 확인
                cnt += 1
            else:  # 최우선 기능이 작업이 완료되지 않으면 뒤에 것은 보지 않고 종료
                break

        if cnt > 0:  # 배포할 기능이 한 개 이상일 때
            for _ in range(cnt):  # 작업 완료한 기능은 제거
                progresses.popleft()
                speeds.popleft()
            answer.append(cnt)  # 배포한 기능 개수 추가
            cnt = 0

        if not progresses:  # 모든 기능을 배포했으면 종료
            break

    return answer


progresses = [95, 90, 99, 99, 80, 99]  # 작업 현황
speeds = [1, 1, 1, 1, 1, 1]  # 작업 속도
print(solution(progresses, speeds))