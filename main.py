import pygame
import random
from pygame import Surface
from pygame.constants import QUIT
from user_api import InputBox
from Hiragana import Hiragana

WIDTH = 600
HEIGHT = 500
FPS = 120

screen: Surface = None
clock = None
textFont = None
background_image = None


def pygameInit(title: str = "japanese_study_demo", bg_pic_dir: str = "media/a.jpg"):

    pygame.init() # init pygame
    pygame.mixer.init()
    pygame.display.set_caption(title)
    global screen, clock, textFont, background_image
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    background_image = pygame.image.load(bg_pic_dir)


if __name__ == "__main__":
    pygameInit("Hiragana_demo")


    romaji, image_path = Hiragana.random_gen() #random gene pic, dir
    background_image = pygame.image.load(image_path)

    inputbox = InputBox(pygame.Rect(200, 400, 140, 32))  #input box
    running = True
    while running:
        clock.tick(FPS)
        screen.fill((255, 255, 255))  # bg color
        screen.blit(background_image, (0, 0))  # show bg

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            user_text = inputbox.dealEvent(event)  # inputbox

            # check input
            if user_text is not None:
                if user_text == romaji:
                    print(f"Correct input: {user_text}")
                    romaji, image_path = Hiragana.random_gen()  # gene new bg, dir
                    background_image = pygame.image.load(image_path)
                elif user_text == 'answer':
                    print(f"answer is: {romaji}")
                else:
                    print(f"Wrong input: {user_text}")

        inputbox.draw(screen)
        pygame.display.flip()

    pygame.quit()
