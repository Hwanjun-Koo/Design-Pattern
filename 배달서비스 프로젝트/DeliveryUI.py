import pygame

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)  # 배경색

# 오토바이 색상
BIKE_COLOR = (0, 0, 255)

# 오토바이 크기와 위치
BIKE_WIDTH, BIKE_HEIGHT = 80, 40
BIKE_X, BIKE_Y = WIDTH // 2, HEIGHT // 2

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Delivery Motorcycle")

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 배경 그리기
    screen.fill(BG_COLOR)
    
    # 오토바이 그리기
    pygame.draw.rect(screen, BIKE_COLOR, (BIKE_X - BIKE_WIDTH // 2, BIKE_Y - BIKE_HEIGHT // 2, BIKE_WIDTH, BIKE_HEIGHT))
    
    # 화면 업데이트
    pygame.display.flip()

# pygame 종료
pygame.quit()