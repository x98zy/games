import sys
import pygame
from settings import Settings
settings=Settings()
def run_game():
    pygame.init()
    screen=pygame.display.set_mode(settings.screen)
    pygame.display.set_caption("外星人入侵")#设置窗口标题
    bg_color=(230,230,230)
    while True:#开始游戏循环
        for event in pygame.event.get():#pygame.event.get()返回值是一个列表
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(settings.color)
        pygame.display.flip()#让最近绘制的屏幕可见
run_game()