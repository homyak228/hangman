import pygame
import settings

def start():
    pygame.init()

    # Настройка
    window = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
    pygame.display.set_caption("Hangman")
    pygame.display.set_icon(pygame.image.load("./assets/sprites/icon.png"))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

if __name__ == "__main__":
    start()