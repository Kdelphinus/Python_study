curr = list(map(int, input().split(":")))
curr_time = curr[0] * 3600 + curr[1] * 60 + curr[2]
start = list(map(int, input().split(":")))
start_time = start[0] * 3600 + start[1] * 60 + start[2]
if curr_time > start_time:
    start_time += 24 * 3600
remained_time = start_time - curr_time
print(f"{remained_time // 3600:02d}", end=":")
remained_time %= 3600
print(f"{remained_time // 60:02d}", end=":")
remained_time %= 60
print(f"{remained_time:02d}")
