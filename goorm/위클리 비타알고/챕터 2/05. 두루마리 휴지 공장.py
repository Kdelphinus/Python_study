num, possible = map(int, input().split())
tissue = list(map(int, input().split()))
tissue.sort(reverse=True)  # 티슈의 길이를 기준으로 내림차순

# 먼저 가장 긴 휴지와 길이를 맞춤
for t in tissue[1:]:
    possible -= tissue[0] - t

if possible < 0:  # 가장 긴 휴지와도 길이를 맞추지 못하면
    print("No way!")  # 맞출 수 없음
else:  # 가장 긴 휴지와 길이를 맞췄다면
    print(tissue[0] + possible // num)  # 남은 휴지를 똑같이 나누어 이어 붙임

