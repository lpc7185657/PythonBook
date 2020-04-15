import sys #退出模块
import pygame #主游戏窗口模块
from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #创建一艘飞船
    ship = Ship(screen)

    #开始游戏的主循环
    while True:
        #监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
        ship.blitme()

run_game()