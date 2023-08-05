"""14889 스타트와 링크"""

from itertools import combinations

n = int(input())  # 축구할 수 있는 인원
stats = [list(map(int, input().split())) for _ in range(n)]
teams = [str(x) for x in range(n)]

start_stats = link_stats = 0
diff = []

teams = list(combinations(teams, n // 2))

start_team = teams[: len(teams) // 2]
link_team = teams[len(teams) // 2 :]
link_team.reverse()  # 편의를 위해 리스트를 뒤집음

for team in range(len(start_team)):
    for member1 in range(n // 2):  # start team stats 구하기
        for member2 in range(member1, n // 2):
            if member1 != member2:
                member_1 = int(start_team[team][member1])
                member_2 = int(start_team[team][member2])

                start_stats = (
                    start_stats + stats[member_1][member_2] + stats[member_2][member_1]
                )

    for member1 in range(n // 2):  # link team stats 구하기
        for member2 in range(member1, n // 2):
            if member1 != member2:
                member_1 = int(link_team[team][member1])
                member_2 = int(link_team[team][member2])

                link_stats = (
                    link_stats + stats[member_1][member_2] + stats[member_2][member_1]
                )

    diff.append(abs(start_stats - link_stats))
    start_stats = link_stats = 0

print(min(diff))
