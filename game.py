import pygame
import settings
from settings import LETTER_HEIGHT, LETTER_OFFSET, LETTER_START_POS


def start_game():
    pygame.init()

    # Настройка
    window = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
    pygame.display.set_caption("Hangman")
    pygame.display.set_icon(pygame.image.load("./assets/sprites/icon.png"))
    game_font = pygame.font.Font("./assets/fonts/HaginCapsMedium-Medium.ttf", 32)

    background_image = pygame.transform.scale(pygame.image.load("./assets/sprites/Wild_west.png"), [settings.WIDTH, settings.HEIGHT])
    letter_button = pygame.transform.scale(pygame.image.load("./assets/sprites/button.png"), [settings.LETTER_WIDTH, settings.LETTER_HEIGHT])
    button_image = pygame.transform.scale(pygame.image.load("./assets/sprites/button.png"), [90, 40])
    no_image = pygame.transform.scale(pygame.image.load("./assets/sprites/no.png"), [30,35])

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x >= 300 and mouse_x <= 390:
                    if mouse_y >= 10 and mouse_y <= 50:
                        run = False

        window.blit(background_image, [0,0])

        # Отрисовка кнопок с буквами
        for x in range(10):
            window.blit(letter_button, [2 + x * (35 + 5), LETTER_START_POS])
            window.blit(game_font.render(str(chr(1072 + x)), True, [255, 138, 0]), [12 + x * (35 + 5), LETTER_START_POS - 5])
        for x in range(10):
            window.blit(letter_button, [2 + x * (35 + 5), LETTER_START_POS + LETTER_HEIGHT + LETTER_OFFSET])
            window.blit(game_font.render(str(chr(1082 + x)), True, [255, 138, 0]), [12 + x * (35 + 5), LETTER_START_POS - 5 + LETTER_HEIGHT + LETTER_OFFSET])
        for x in range(10):
            window.blit(letter_button, [2 + x * (35 + 5), LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 2])
            window.blit(game_font.render(str(chr(1092 + x)), True, [255, 138, 0]), [12 + x * (35 + 5), LETTER_START_POS - 5 + (LETTER_HEIGHT + LETTER_OFFSET) * 2])
        for x in range(2):
            window.blit(letter_button, [150 + x * (35 + 5), LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 3])
            window.blit(game_font.render(str(chr(1102 + x)), True, [255, 138, 0]), [160 + x * (35 + 5), LETTER_START_POS - 5 + (LETTER_HEIGHT + LETTER_OFFSET) * 3])

        window.blit(button_image, [300, 10])
        window.blit(game_font.render("Выход", True, [255, 65, 0]), [305, 10])

        pygame.display.update()

if __name__ == "__main__":
    start_game()
    pygame.quit()