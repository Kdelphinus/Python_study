def ccw(p1, p2, p3):
    """ccw Counter ClockWise
        외적 설명 링크: http://dolphin.ivyro.net/file/mathematics/tutorial09.html

    Args:
        p1 (list): 주어진 점의 위치 1
        p2 (list): 주어진 점의 위치 2
        p3 (list): 주어진 점의 위치 3

    Returns:
        (int): 음수면 시계방향(밑으로 또는 안으로), 양수면 반시계방향(위로 또는 밖으로)으로 회전
    """
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (
        p3[0] * p2[1] + p2[0] * p1[1] + p1[0] * p3[1]
    )


num = int(input())
positions = [list(map(float, input().split())) for _ in range(num)]
p1 = [0.0, 0.0]
p2 = [1.0, 1.0]

for p3 in positions[2:]:
    if ccw(p1, p2, p3) < 0:
        print("RIGHT")
    else:
        print("LEFT")
    p1, p2 = p2, p3
