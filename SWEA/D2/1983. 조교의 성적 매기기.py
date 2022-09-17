test = int(input())

for t in range(test):
    n, k = map(int, input().split())
    scores = []

    for i in range(n):  # 총점 계산
        middle, final, assign = map(int, input().split())
        score = middle * 0.35 + final * 0.45 + assign * 0.2
        scores.append([i + 1, score])  # 현 위치, 총점

    scores.sort(key=lambda x: -x[1])  # 총점으로 내림차순

    for i in range(len(scores)):  # 현재 있는 인덱스 + 1이 등수
        if scores[i][0] == k:
            rank = i + 1
            break

    if rank <= n / 10:
        print("#{} A+".format(t + 1))
    elif rank <= n / 10 * 2:
        print("#{} A0".format(t + 1))
    elif rank <= n / 10 * 3:
        print("#{} A-".format(t + 1))
    elif rank <= n / 10 * 4:
        print("#{} B+".format(t + 1))
    elif rank <= n / 10 * 5:
        print("#{} B0".format(t + 1))
    elif rank <= n / 10 * 6:
        print("#{} B-".format(t + 1))
    elif rank <= n / 10 * 7:
        print("#{} C+".format(t + 1))
    elif rank <= n / 10 * 8:
        print("#{} C0".format(t + 1))
    elif rank <= n / 10 * 9:
        print("#{} C-".format(t + 1))
    else:
        print("#{} D0".format(t + 1))