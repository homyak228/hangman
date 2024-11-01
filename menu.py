import pygame
import settings
from game import start_game

def start_menu():
    pygame.init()

    # Настройка
    window = pygame.display.set_mode([settings.WIDTH,settings.HEIGHT])
    pygame.display.set_caption("Hangman")
    pygame.display.set_icon(pygame.image.load("./assets/sprites/icon.png"))
    menu_font = pygame.font.Font("./assets/fonts/HaginCapsMedium-Medium.ttf", 50)

    # Загрузка спрайтов
    background_image = pygame.transform.scale(pygame.image.load("./assets/sprites/Wild_west.png"), [settings.WIDTH, settings.HEIGHT])
    button_image = pygame.transform.scale(pygame.image.load("./assets/sprites/button.png"), [settings.BUTTON_WIDTH, settings.BUTTON_HEIGHT])

    # Загрузка музыки
    pygame.mixer.music.load("./assets/sounds/Background_music.mp3")
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(1, 0, 0)
    click = pygame.mixer.Sound("./assets/sounds/click.mp3")

    run = True
    while run:
        # Обработка событий
        for event in pygame.event.get():
            # Выход из приложения
            if event.type == pygame.QUIT:
                run = False
            # Проверка нажатия на кнопку
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Получение координат курсора
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Проверка нажатия на кнопку играть
                if mouse_x >= 105 and mouse_x <= 105 + settings.BUTTON_WIDTH:
                    if mouse_y >= 170 and mouse_y <= 230:
                        click.play()
                        start_game()
                        run = False

                # Проверка нажатия на кнопку выйти
                if mouse_x >= 105 and mouse_x <= 105 + settings.BUTTON_WIDTH:
                    if mouse_y >= 260 and mouse_y <= 320:
                        run = False

        # Отрисовка фона
        window.blit(background_image, [0,0])

        # Отрисовка кнопки играть
        window.blit(button_image, [105,170])
        window.blit(menu_font.render("Играть", True, [255, 138, 0]), [130,168])
        # Отрисовка кнопки выйти
        window.blit(button_image, [105, 260])
        window.blit(menu_font.render("Выйти", True, [255, 65, 0]), [130, 258])

        # Отрисовка логотипа
        window.blit(menu_font.render("Виселица", True, [255, 210, 0]), [98, 25])

        # Обновление экрана
        pygame.display.update()

if __name__ == "__main__":
    start_menu()
    pygame.quit()