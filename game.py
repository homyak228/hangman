import pygame
import settings
from settings import LETTER_HEIGHT, LETTER_OFFSET, LETTER_START_POS, LETTER_WIDTH, MAX_ATTEMPTS, BUTTON_WIDTH, \
    BUTTON_HEIGHT, WORDS
import random

def check_letter(letter: str, word: str):
    output = []
    counter = 0
    for x in word:
        if x == letter:
            output.append(counter)
        counter += 1
    print(output)
    return output

def to_string(string: list):
    output = ""
    for x in string:
        output += x
    return output

def start_game():
    pygame.init()

    # Настройка
    window = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT])
    pygame.display.set_caption("Hangman")
    pygame.display.set_icon(pygame.image.load("./assets/sprites/icon.png"))
    game_font = pygame.font.Font("./assets/fonts/HaginCapsMedium-Medium.ttf", 32)
    word = random.choice(settings.WORDS)
    guessing_word = list(len(word) * "_")
    attempts = MAX_ATTEMPTS
    no_image_pos = []
    game_over = False

    # Згрузка ассетов
    background_image = pygame.transform.scale(pygame.image.load("./assets/sprites/Wild_west.png"), [settings.WIDTH, settings.HEIGHT])
    letter_button = pygame.transform.scale(pygame.image.load("./assets/sprites/button.png"), [settings.LETTER_WIDTH, settings.LETTER_HEIGHT])
    button_image = pygame.transform.scale(pygame.image.load("./assets/sprites/button.png"), [90, 40])
    no_image = pygame.transform.scale(pygame.image.load("./assets/sprites/no.png"), [30,35])
    click = pygame.mixer.Sound("./assets/sounds/click.mp3")
    word_guess_bg = pygame.transform.scale(pygame.image.load("assets/sprites/word-guessing-bg.png"), [360,40])

    # Основной цикл игры
    run = True
    while run:
        for event in pygame.event.get(): # Обработка условий
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Проверка нажатия на кнопку выхода
                if mouse_x >= 300 and mouse_x <= 390:
                    if mouse_y >= 10 and mouse_y <= 50:
                        run = False
                # Проверка нажатия на кнопки с буквами
                for x in range(10):
                    if mouse_x >= 2 + x * (35+5) and mouse_x <= (2 + x * (35+5)) + LETTER_WIDTH:
                        if mouse_y >= LETTER_START_POS and mouse_y <= LETTER_START_POS + LETTER_HEIGHT:
                            print(str(chr(1072 + x)))
                            click.play()
                            if check_letter(str(chr(1072 + x)), word.lower()) != []:
                                for t in check_letter(str(chr(1072 + x)), word.lower()):
                                    guessing_word[t] = word[t]
                            else:
                                attempts -= 1
                                no_image_pos.append([2 + x * (35 + 5), LETTER_START_POS])
                for y in range(10):
                    if mouse_x >= 2 + y * (35+5) and mouse_x <= (2 + y * (35+5)) + LETTER_WIDTH:
                        if mouse_y >= LETTER_START_POS + LETTER_HEIGHT + LETTER_OFFSET and mouse_y <= (LETTER_START_POS + LETTER_HEIGHT + LETTER_OFFSET) + LETTER_HEIGHT:
                            print(str(chr(1082 + y)))
                            click.play()
                            if check_letter(str(chr(1082 + y)), word.lower()) != []:
                                for t in check_letter(str(chr(1082 + y)), word.lower()):
                                    guessing_word[t] = word[t]
                            else:
                                attempts -= 1
                                no_image_pos.append([2 + y * (35 + 5), LETTER_START_POS + LETTER_HEIGHT + LETTER_OFFSET])
                for z in range(10):
                    if mouse_x >= 2 + z * (35 + 5) and mouse_x <= (2 + z * (35 + 5)) + LETTER_WIDTH:
                        if mouse_y >= LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 2 and mouse_y <= (LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 2) + LETTER_HEIGHT:
                            click.play()
                            print(str(chr(1092 + z)))
                            if check_letter(str(chr(1092 + z)), word.lower()) != []:
                                for t in check_letter(str(chr(1092 + z)), word.lower()):
                                    guessing_word[t] = word[t]
                            else:
                                attempts -= 1
                                no_image_pos.append(
                                    [2 + z * (35 + 5), LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 2])
                for a in range(2):
                    if mouse_x >= 150 + a * (35 + 5) and mouse_x <= (150 + a * (35 + 5)) + LETTER_WIDTH:
                        if mouse_y >= LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 3 and mouse_y <= (LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 3) + LETTER_HEIGHT:
                            print(str(chr(1102 + a)))
                            click.play()
                            if check_letter(str(chr(1102 + a)), word.lower()) != []:
                                for t in check_letter(str(chr(1102 + a)), word.lower()):
                                    guessing_word[t] = word[t]
                            else:
                                attempts -= 1
                                no_image_pos.append(
                                    [150 + a * (35 + 5), LETTER_START_POS + (LETTER_HEIGHT + LETTER_OFFSET) * 3])
                if mouse_x >= 140 and mouse_x <= 140 + BUTTON_WIDTH:
                    if mouse_y >= 100 and mouse_y <= 100 + BUTTON_HEIGHT:
                        if game_over:
                            click.play()
                            attempts = MAX_ATTEMPTS
                            no_image_pos = []
                            word = random.choice(WORDS)
                            guessing_word = list(len(word) * "_")
                            game_over = False
        # Отрисовка фона
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
        # Отрисовка кнопки выход
        window.blit(button_image, [300, 10])
        window.blit(game_font.render("Выход", True, [255, 65, 0]), [305, 10])

        for x in no_image_pos:
            window.blit(no_image, x)

        if attempts <= 0:
            window.blit(game_font.render("Вы проиграли!", True, [0, 65, 65]), [100, 60])
            window.blit(game_font.render(f"Загаданное слово: {word}", True, [0, 65, 65]), [20, 90])
            window.blit(button_image, [140, 130])
            window.blit(game_font.render("Ещe!", True, [255, 65, 0]), [155, 130])
            game_over = True

        if to_string(guessing_word) == word and attempts > 0:
            window.blit(game_font.render("Вы победили!", True, [0,255,0]), [100,60])
            window.blit(button_image, [140, 100])
            window.blit(game_font.render("Ещe!", True, [255, 65, 0]), [155, 100])
            game_over = True

        window.blit(word_guess_bg, [20, LETTER_START_POS - LETTER_OFFSET * 2 - LETTER_HEIGHT])
        window.blit(game_font.render(to_string(guessing_word), True, [255, 0, 50]), [20, LETTER_START_POS - LETTER_OFFSET * 2 - LETTER_HEIGHT])
        # Обновление экрана
        pygame.display.update()

if __name__ == "__main__":
    start_game()
    pygame.quit()