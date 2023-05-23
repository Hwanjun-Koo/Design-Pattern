import pygame
import sys

# 초기화
pygame.init()

# 창 크기 설정
screen = pygame.display.set_mode((800, 600))

# 배달원 위치 초기화
deliverer_position = [0, 300]

# 이동 속도 설정 (픽셀/초)
speed = 800 // 10  # 스크린을 가로지르는 데 10초 걸리도록 설정

# 시계 객체 생성
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 배경색을 검은색으로 설정
    screen.fill((0, 0, 0))

    # 배달원의 위치 업데이트
    deliverer_position[0] += speed * (clock.get_time() / 1000)  # 속도 * 시간 = 이동 거리

    # 배달원 그리기 (여기서는 간단하게 사각형으로 그립니다)
    pygame.draw.rect(screen, (255, 255, 255), (*deliverer_position, 50, 50))

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 간 시간 측정
    clock.tick(60)