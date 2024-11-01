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
wrong_count = 0


def pygameInit(title: str = "japanese_study_demo", bg_pic_dir: str = "media/a.jpg"):
    pygame.init()  # Initialize pygame
    pygame.mixer.init()
    pygame.display.set_caption(title)
    global screen, clock, textFont, background_image
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    try:
        background_image = pygame.image.load(bg_pic_dir)
    except pygame.error:
        print(f"Failed to load background image from {bg_pic_dir}. Using a solid color instead.")
        background_image = pygame.Surface((WIDTH, HEIGHT))
        background_image.fill((255, 255, 255))  # Use white background if image fails to load

pygameInit("Hiragana_demo")

romaji, image_path = Hiragana.random_gen()  # Randomly generate romaji and image path
try:
    background_image = pygame.image.load(image_path)
except pygame.error:
    print(f"Failed to load hiragana image from {image_path}. Using default background.")

inputbox = InputBox(pygame.Rect(200, 400, 140, 32))  # Input box for user input
running = True
while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))  # Set background color
    screen.blit(background_image, (0, 0))  # Display background image

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        user_text = inputbox.dealEvent(event)  # Handle input box events

        # Check user input
        if user_text is not None:
            if user_text == romaji:
                print(f"Correct input: {user_text}")
                romaji, image_path = Hiragana.random_gen()  # Generate new romaji and image
                try:
                    background_image = pygame.image.load(image_path)
                except pygame.error:
                    print(f"Failed to load hiragana image from {image_path}. Using default background.")
                wrong_count = 0
            elif user_text == 'answer':
                print(f"The correct answer is: {romaji}")
            else:
                wrong_count += 1
                print(f"Wrong input: {user_text}")
                if wrong_count == 3:
                    print(f"The correct answer is: {romaji}")

    inputbox.draw(screen)
    pygame.display.flip()

pygame.quit()
