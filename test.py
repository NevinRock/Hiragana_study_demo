import pygame
from pygame import Surface
from pygame.constants import QUIT

from user_api import InputBox

WIDTH = 600
HEIGHT = 500
FPS = 120

screen: Surface = None  # 窗口实例
clock = None  # 时钟实例

textFont = None  # 字体


def pygameInit(title: str = "japanese_study_demo", bg_pic_dir: str = "media/a.jpg"):
    """初始化 pygame"""
    pygame.init()
    pygame.mixer.init()  # 声音初始化
    pygame.display.set_caption(title)
    global screen, clock, textFont, background_image  # 修改全局变量
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    background_image = pygame.image.load(bg_pic_dir)

if __name__ == "__main__":
    pygameInit("输入框示例")
    inputbox = InputBox(pygame.Rect(200, 400, 32, 32))  # 输入框
    running = True
    while running:
        clock.tick(FPS)  # 限制帧数
        screen.fill((255, 255, 255))  # 铺底
        screen.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            user_text = inputbox.dealEvent(event)  # 输入框处理事件
            if user_text != None:
                print(f"this is:{user_text}")

        inputbox.draw(screen)  # 输入框显示
        pygame.display.flip()
    pygame.quit()
