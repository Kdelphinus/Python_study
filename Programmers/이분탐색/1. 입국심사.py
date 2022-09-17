"""이분 탐색의 기준을 잘 선택하기"""
# 링크: https://sohee-dev.tistory.com/123


def solution(n, times):
    answer = 0
    short, long = 1, max(times) * n  # 최소 시간, 최대 시간

    while short <= long:
        cnt = 0
        mid = (short + long) // 2

        # 각 심사대별로 mid시간동안 할 수 있는 입국심사
        for time in times:
            cnt += mid // time
            if cnt >= n:  # 해야할 인원을 넘어가면 반복문 종료
                break

        if cnt >= n:  # 해야할 인원을 넘어가면 시간을 더 줄일 수 있는지 확인
            long = mid - 1
            answer = mid  # 현재 시간은 저장
        else:  # 해야할 인원을 못 넘기면 시간을 더 늘려서 확인
            short = mid + 1

    return answer
