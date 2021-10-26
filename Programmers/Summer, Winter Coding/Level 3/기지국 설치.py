"""Summer/Winter Coding(~2018)"""


def solution(n, stations, w):
    answer = 0
    next_start = 1  # 다음 시작 위치
    s_range = (w * 2) + 1  # 공유기 범위
    for station in stations:
        now_end = station - w - 1  # 현재 확인할 범위의 끝
        now_start = next_start  # 현재 확인할 범위의 시작
        next_start = station + w + 1  # 다음에 확인할 범위의 시작

        if now_start <= now_end and now_end > 0:  # 범위가 유효하다면
            answer += (now_end - now_start) // s_range + 1  # 그 안에 최소 공유기 개수 설치

    if now_end <= n:  # 마지막쪽을 확인 안 했다면 확인
        answer += (n - next_start) // s_range + 1

    return answer


# -----------------------------------------------------------------------------------

"""다른 풀이"""


def solution(n, stations, w):
    ans = 0
    idx = 0  # station index
    location = 1  # 현재 위치

    while location <= n:  # 주어진 위치 안에 location이 있어야 한다
        # 이미 설치된 기지국 범위 내라면 다음 기지국으로 이동
        if idx < len(stations) and location >= stations[idx] - w:
            location = stations[idx] + w + 1
            idx += 1
        # 이미 설치된 기지국 범위 밖이라면 설치하고 다음 범위로 이동
        else:
            location += 2 * w + 1
            ans += 1
    return ans
