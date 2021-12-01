# 부분합을 이용
length = int(input())  # 제설할 도로의 길이
snow_height = list(map(int, input().split()))  # 도로마다 쌓인 눈의 높이
shovel_num = int(input())  # 삽의 개수
snow_shovels = sorted(list(map(int, input().split())))  # 각 삽의 너비
rock_num = int(input())  # 바위의 개수
rocks = sorted(list(map(int, input().split())))  # 각 바위들의 위치

prefix_sum = [0] * (length + 1)  # 부분합을 저장할 리스트
for idx in range(1, length + 1):
    # 계속해서 합친다
    prefix_sum[idx] = prefix_sum[idx - 1] + snow_height[idx - 1]

min_shovel, max_snows = 0, 0
for shovel in snow_shovels:
    idx = 0  # 바위의 위치를 확인할 인덱스
    start = 1  # 제설 시작 위치
    while start + shovel - 1 <= length:  # 삽이 도로 밖으로 벗어나면 안 된다
        # 바위가 더이상 없거나 바위가 삽에 걸리지 않을 때
        if idx >= rock_num or rocks[idx] > start + shovel - 1:
            # 더 많이 제설할 수 있다면 최신화
            if (
                max_snows
                < prefix_sum[start + shovel - 1] - prefix_sum[start - 1]
            ):
                max_snows = (
                    prefix_sum[start + shovel - 1] - prefix_sum[start - 1]
                )
                min_shovel = shovel
            start += 1  # 다음 위치로 이동

        # 바위에 걸려 다음 바위로 이동해야 할 때
        elif idx < rock_num:
            start = rocks[idx] + 1
            idx += 1
        # 너비가 안 되지만 바위에 걸리지도 않을 때
        else:
            start += 1

print(min_shovel, max_snows)
