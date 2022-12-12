# 링크: https://ku-hug.tistory.com/148
# 시간 복잡도에 미리 겁먹지 말자
import sys

INPUT = sys.stdin.readline


def party(party_num: int, no_lie: set) -> int:
    cnt, parties = 0, []
    for _ in range(party_num):
        parties.append(set(INPUT().split()[1:]))

    for _ in range(party_num):
        for party in parties:
            if party & no_lie:
                no_lie = no_lie.union(party)

    for party in parties:
        if party & no_lie:
            continue
        cnt += 1

    return cnt


if __name__ == "__main__":
    N, M = map(int, INPUT().split())
    true_people = list(INPUT().split())
    print(M) if len(true_people) == 1 else print(party(M, set(true_people[1:])))
