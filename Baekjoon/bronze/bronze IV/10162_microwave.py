cooking_time = int(input())
button = [[300, 0], [60, 0], [10, 0]]
for i in range(3):
    button[i][1] += cooking_time // button[i][0]
    cooking_time %= button[i][0]
if cooking_time == 0:
    for c_time, cnt in button:
        print(cnt, end=" ")
else:
    print(-1)
