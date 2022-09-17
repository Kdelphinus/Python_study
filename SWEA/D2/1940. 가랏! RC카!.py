test = int(input())

for t in range(test):
    num = int(input())
    commands = [list(map(int, input().split())) for _ in range(num)]
    dist = 0
    speed = 0

    for command in commands:
        if command[0] == 0:
            dist += speed
        elif command[0] == 1:
            speed += command[1]
            dist += speed
        else:
            if speed > command[1]:
                speed -= command[1]
            else:
                speed = 0
            dist += speed

    print("#{} {}".format(t + 1, dist))
