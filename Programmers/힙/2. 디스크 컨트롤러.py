"""나의 풀이"""


def solution(jobs):
    answer = 0
    idx = 1
    jobs.sort(key=lambda x: (x[0], x[1]))  # 요청한 시간, 소요 시간을 기준으로 정렬
    time = jobs[0][0]  # 시간은 첫 작업시간으로 초기화
    watting = [jobs[0]]  # 첫 작업 삽입

    while watting or idx < len(jobs):
        if not watting:  # 만약 대기 작업이 없으나 모든 작업이 끝나지 않았을 때
            watting.append(jobs[idx])  # 다음 작업을 넣고
            time = jobs[idx][0]  # 현재 시간을 다음 작업이 요청된 시간으로 변경한 뒤
            idx += 1  # index 이동
        else:  # 대기 작업이 남아있을 때
            watting.sort(key=lambda x: (x[1], x[0]))  # 대기 작업을 소요 시간, 요청한 시간으로 정렬
            next_job = watting.pop(0)  # 가장 우선시 되는 작업을 실행
            time += next_job[1]  # 소요 시간만큼 시간 진행
            answer += time - next_job[0]  # 종료 시간 - 요청한 시간

        # 현재 작업이 진행 중일 때, 작업이 요청되면 대기열에 추가
        while idx < len(jobs):
            job = jobs[idx]
            if time < job[0]:  # 현재 작업이 끝난 후면 반복문 종료
                break
            watting.append(job)
            idx += 1

    return answer // len(jobs)


# ----------------------------------------------------------------------------------------------------------------

"""힙을 사용한 풀이"""
import heapq
from collections import deque


def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0

    while len(q) > 0:
        # 현재 작업을 실행
        dur, arr = heapq.heappop(q)  # 소요 시간, 요청된 시간
        current_time = max(current_time + dur, arr + dur)  # 현재시간에서 바로 실행 안 된 경우를 대비
        total_response_time += current_time - arr  # 총 소요 시간

        # 요청된 작업이 남아있고 그 작업이 다른 작업이 진행 중일 때 요청된 것이면 작업 목록에서 힙으로 이동
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())

        # 요청된 작업이 남아있으나 힙 비어있으면 작업 목록에서 힙으로 이동
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())

    return total_response_time // len(jobs)


print(solution([[0, 3], [1, 9], [2, 5]]))
