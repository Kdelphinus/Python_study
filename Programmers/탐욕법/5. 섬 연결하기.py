# 크루스칼 알고리즘을 활용
# 해답: https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=jaeyoon_95&logNo=221872563653&categoryNo=74&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    connections = [costs[0][0]]

    while len(connections) < n:
        for idx, cost in enumerate(costs):
            # 두 섬 중 한 섬만 다리가 놓여져 있을 때
            if cost[0] in connections or cost[1] in connections:
                answer += cost[2]  # 다리를 짓고
                connections.append(cost[0])  # 섬 추가
                connections.append(cost[1])  # 섬 추가

                connections = list(set(connections))  # 중복 제거
                costs.pop(idx)  # 현재 다리는 건설했으므로 제거
                break  # costs 최신화하여 다시 확인

    return answer
