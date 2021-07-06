import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)  # 힙으로 만듬

    while len(scoville) > 1:  # 힙의 원소가 2개보다 작으면 더이상 더할 수 없다
        if scoville[0] >= K:  # 최소값이 K보다 크면 종료
            return answer

        answer += 1  # 섞는 횟수를 올리고
        tmp = heapq.heappop(scoville)  # 최솟값을 꺼낸다
        tmp += heapq.heappop(scoville) * 2  # 두 번째 작은 숫자도 꺼내 주어진 식대로 계산한다
        heapq.heappush(scoville, tmp)  # 구한 값을 다시 집어넣는다

    if scoville[0] >= K:  # 만약 원소가 2개보다 작지만 모두 K를 넘을 때
        return answer

    return -1  # 아니라면


print(solution([1, 2, 3, 9, 10, 12], 7))

# -------------------------------------------------------------------------
# 모범답안
import heapq as hq


def solution(scoville, K):

    hq.heapify(scoville)  # 힙으로 만듬
    answer = 0
    while True:
        first = hq.heappop(scoville)  # 최솟값을 빼서 저장
        if first >= K:  # 최솟값이 K보다 크다면 반복문 종료
            break
        if len(scoville) == 0:  # 모든 음식을 다 썼다면 K를 넘을 수 없으므로 -1리턴
            return -1
        second = hq.heappop(scoville)  # 두번째 최솟값을 뺴서 저장
        hq.heappush(scoville, first + second * 2)  # 주어진 식대로 계산해 저장
        answer += 1  # 섞은 횟수 추가

    return answer  # 총 섞은 횟수 리턴
