"""7568 덩치"""

# 전체 사람 수
num = int(input())

# 전체 사람의 몸무게와 키를 담을 리스트
masses = []

# 덩치 순위를 담을 리스트
rank = []

# 각 사람의 몸무게와 키
for i in range(num):
    mass = list(map(int, input().split()))
    masses.append(mass)

# 덩치 순위 부여
for i in range(len(masses)):
    cnt = 1
    for j in range(len(masses)):
        if masses[i][0] < masses[j][0] and masses[i][1] < masses[j][1]:
            cnt += 1
    rank.append(cnt)

# 덩치 순위 출력
for i in rank:
    print(i, end=" ")
