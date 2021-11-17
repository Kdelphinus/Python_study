from collections import deque

def bfs(here, height, width):
    """bfs 불이 번지는 시간을 구하는 함수

    Args:
        here (tulpe): 사람의 위치
        height (int): 방의 세로 길이
        width (int): 방의 가로 길이

    Returns:
        sec (int): 사람이 있는 곳까지 불이 번지는 시간
        -1 (int): 사람이 있는 곳까지 불이 번지지 않을 경우 
    """
    queue = deque(fires) # 초기 불이 난 위치를 큐로 전환
    dx = [1, -1, 0, 0] # 가로 행동 반경
    dy = [0, 0, 1, -1] # 세로 행동 반경

    while queue: # 모두 번질 때까지
        y, x, sec = queue.popleft() # 확인해야 할 불 정보 꺼냄
        
        for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            
            if (ny, nx) == here: # 불이 사람한테 도달했을 때
                return sec # 도달한 시간 리턴
            
            # 방 반경을 벗어나지 않고 불이 번질 수 있는 위치일 때
            if 0 <= ny < height and 0 <= nx < width and room[ny][nx] == '.':
                room[ny][nx] = '@' # 불 번짐 표시
                queue.append((ny, nx, sec + 1)) # 다음 탐색할 위치로 추가
        
    return -1 # 모두 번질 때까지 사람에게 번지지 않을 때

height, width = map(int, input().split()) # 방의 세로 길이와 가로 길이
room = [[] for _ in range(height)] # 방의 구조
fires = [] # 초기 불이 난 구역
for h in range(height):
	tmp = input()
	for w, t in enumerate(tmp):
		if t == '&': # 사람의 위치 저장
			here = (h, w)
		if t == '@': # 불이 난 위치 저장
			fires.append((h, w, 0)) # (행, 열, 시간)
		room[h].append(t)

print(bfs(here, height, width))



	
