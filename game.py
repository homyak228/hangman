import pygame
import settings


def start():
    pygame.init()

    # Настройка
    window = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
    pygame.display.set_caption("Hangman")
    pygame.display.set_icon(pygame.image.load("./assets/sprites/icon.png"))

    background_image = pygame.transform.scale(pygame.image.load("./assets/sprites/Wild_west.png"), [settings.WIDTH, settings.HEIGHT])

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(background_image, [0,0])

        pygame.display.update()

if __name__ == "__main__":
    start()