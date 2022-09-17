def solution(routes):
    routes.sort(key=lambda x: x[1])  # 나가는 것을 기준으로 정렬해야 함
    limit = -float("inf")
    cctv = []

    for start, end in routes:
        if limit < start:
            limit = end
            cctv.append(limit)

    return len(cctv)
