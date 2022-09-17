"""나의 풀이"""


def solution(begin, target, words):
    if target not in words:  # 단어가 없으면 바꿀 수 없다
        return 0

    answer = 0
    stack = [begin]
    visited = [False] * len(words)

    while stack:
        now = stack.pop()

        if now == target:  # 목표 단어로 변환됐으면 바로 종료
            return answer

        for i in range(len(words)):
            if not visited[i]:  # 아직 탐색하지 않은 단어일 때
                diff = 0
                for a, b in zip(now, words[i]):  # 다른 단어의 수 계산
                    if a != b:
                        diff += 1

                if diff == 1:  # 한 글자만 다르다면 그 단어로 변환하는 방법도 구함
                    stack.append(words[i])
                    visited[i] = True
        answer += 1

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

# --------------------------------------------------------------------------------------------------

"""다른 답안"""

from collections import deque


def get_adjacent(current, words):
    """글자 차이가 한 글자인지 확인해주는 함수"""
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        print(get_adjacent(current, words))

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
