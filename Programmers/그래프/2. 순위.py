# 플로이드-와셜 함수를 이용
# 답안: https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%9E%98%ED%94%84-Floyd-Warshall-Level3


def solution(n, results):
    answer = 0

    # graph[a][b]: a가 b에 대한 전적
    # 승리: True, 패배: False, 전적없음: None
    graph = [[None] * n for _ in range(n)]
    for win, lose in results:
        graph[win - 1][lose - 1] = True
        graph[lose - 1][win - 1] = False

    # start_p와 way_p의 전적과 way_P와 end_p의 전적이 똑같다면 start_p와 end_p의 전적도 알 수 있다
    for way_p in range(n):
        for start_p in range(n):
            for end_p in range(n):
                if graph[start_p][way_p] == None:
                    continue

                if graph[start_p][way_p] == graph[way_p][end_p]:
                    graph[start_p][end_p] = graph[start_p][way_p]
                    graph[end_p][start_p] = not graph[start_p][way_p]

    # 자신을 제외한 전적이 모두 있을 때만 순위를 추측할 수 있다
    for i in range(n):
        if None in graph[i][:i] + graph[i][i + 1 :]:
            continue
        answer += 1

    return answer
