import pygame
import sys

# 初始化 Pygame
pygame.init()

# 定義顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 設定遊戲視窗大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("簡單的 Pygame 遊戲")

# 定義玩家方塊
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size

# 設定玩家方塊的速度
player_speed = 5

# 遊戲主迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 獲取鍵盤輸入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # 清除畫面
    screen.fill(BLACK)

    # 繪製玩家方塊
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))

    # 更新畫面
    pygame.display.flip()

    # 控制遊戲更新速率
    pygame.time.Clock().tick(60)
