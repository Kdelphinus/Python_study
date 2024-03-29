# 버블 발사
import pygame
import os, random, math


# 버블 클래스 생성
class Bubble(pygame.sprite.Sprite):
    def __init__(self, image, color, position=(0, 0)):
        super().__init__()
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position)
        self.radius = 18  # 버블 이동을 위한 반지름

    def set_rect(self, position):
        self.rect = self.image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_angle(self, angle):
        self.angle = angle
        self.rad_angle = math.radians(self.angle)  # 라디안으로 변환

    def move(self):
        to_x = self.radius * math.cos(self.rad_angle)
        to_y = self.radius * math.sin(self.rad_angle) * -1

        self.rect.x += to_x
        self.rect.y += to_y

        # 벽에 부딪쳤을 때
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.set_angle(180 - self.angle)


# 발사대 클래스 생성
class Pointer(pygame.sprite.Sprite):
    def __init__(self, image, position, angle):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.angle = angle
        self.original_image = image  # 항상 0도를 바라보는 이미지
        self.position = position

    # 스크린에 띄우기
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # 회전
    def rotate(self, angle):
        self.angle += angle

        if self.angle > 170:
            self.angle = 170
        elif self.angle < 10:
            self.angle = 10

        # 원본 이미지를 각도만큼 회전시켜서 저장
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)

        # 포인터의 중심이 항상 고정되도록(바뀌는 이미지에 계속 중심을 맞춰줌)
        self.rect = self.image.get_rect(center=self.position)


# 맵 만들기
def setup():
    global map
    map = [
        list("RRYYBBGG"),
        list("RRYYBBG/"),  # /: 버블이 위치할 수 없는 곳
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"),  # .: 비어 있는 곳
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
    ]

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in [".", "/"]:
                continue

            position = get_bubble_position(row_idx, col_idx)
            image = get_bubble_image(col)
            bubble_group.add(Bubble(image, col, position))


def get_bubble_position(row_idx, col_idx):
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)

    if row_idx % 2 == 1:
        pos_x += CELL_SIZE // 2

    return pos_x, pos_y


def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    if color == "Y":
        return bubble_images[1]
    if color == "B":
        return bubble_images[2]
    if color == "G":
        return bubble_images[3]
    if color == "P":
        return bubble_images[4]
    return bubble_images[-1]  # 검정


def prepare_bubbles():
    global curr_bubble
    curr_bubble = create_bubble()  # 새 버블 만들기
    curr_bubble.set_rect((screen_width // 2, 624))  # 화살표 중간에 버블 위치


def create_bubble():
    color = get_random_bubble_color()
    image = get_bubble_image(color)

    return Bubble(image, color)


def get_random_bubble_color():
    colors = []
    for row in map:
        for col in row:
            if col not in colors and col not in [".", "/"]:
                colors.append(col)

    return random.choice(colors)


pygame.init()
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)  # 지금 실행하는 파일의 경로
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 버블 이미지 불러오기
bubble_images = [
    pygame.image.load(os.path.join(current_path, "red.png")).convert_alpha(),  # 투명도 처리
    pygame.image.load(os.path.join(current_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "purple.png")).convert_alpha(),
    pygame.image.load(os.path.join(current_path, "black.png")).convert_alpha(),
]

# 발사대 이미지 불러오기
pointer_image = pygame.image.load(os.path.join(current_path, "pointer.png"))
pointer = Pointer(pointer_image, (screen_width // 2, 624), 90)

# 게임 관련 변수
CELL_SIZE = 56
BUBBLE_WIDTH = 56
BUBBLE_HEIGHT = 62
RED = (255, 0, 0)

# 화살표 관련 변수
# 두 키가 눌린 상태에서 한 키를 떼면 바로 움직이도록 설정
to_angle_left = 0  # 왼쪽으로 움직일 각도 정보
to_angle_right = 0  # 오른쪽으로 움직일 각도 정보
angle_speed = 1.5  # 1.5도씩 움직임

curr_bubble = None  # 이번에 쏠 버블
fire = False  # 발사 여부

map = []  # 맵
bubble_group = pygame.sprite.Group()
setup()  # 초기 세팅

running = True
while running:
    clock.tick(60)  # FPS 60으로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_angle_left += angle_speed
            elif event.key == pygame.K_RIGHT:
                to_angle_right -= angle_speed
            elif event.key == pygame.K_SPACE:
                if curr_bubble and not fire:
                    fire = True
                    curr_bubble.set_angle(pointer.angle)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_angle_left = 0
            elif event.key == pygame.K_RIGHT:
                to_angle_right = 0

    if not curr_bubble:
        prepare_bubbles()

    screen.blit(background, (0, 0))
    bubble_group.draw(screen)  # bubble group에 있는 버블 생성
    pointer.rotate(to_angle_left + to_angle_right)  # pointer 회전
    pointer.draw(screen)  # pointer 생성
    if curr_bubble:
        if fire:
            curr_bubble.move()
        curr_bubble.draw(screen)

        # 버블이 화면 밖으로 나갈 때, 현재 충돌이 없기에 밖으로 나가버림
        if curr_bubble.rect.top <= 0:
            curr_bubble = None
            fire = False

    pygame.display.update()

pygame.quit()
