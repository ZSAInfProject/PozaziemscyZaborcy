import pygame
import settings
from button import Button


def menu(GAME):

    menu_exit = False

    while not menu_exit:

        key_red, key_green = False, False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    key_red = True
                elif event.key == pygame.K_x:
                    key_red = True
                elif event.key == pygame.K_z:
                    key_green = True

        GAME.game_display.fill((255, 255, 255))
        myfont = pygame.font.SysFont('monospace', 30)
        label = myfont.render("Pozaziemscy zaborcy", 1, (0, 0, 0))
        GAME.game_display.blit(label, ((GAME.screen_x - label.get_width()) / 2, GAME.screen_y * 0.1))
        menu_exit = check_mouse(GAME, menu_exit, key_red, key_green)

        pygame.display.update()


def check_mouse(GAME, menu_exit, key_RED, key_GREEN):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_width = 200
    button_x = (GAME.screen_x - button_width) * 0.5
    button_height = 60
    button_y = (GAME.screen_y - button_height) * 0.5
    button_offset = button_height + 30
    colours = {"green": (0, 255, 0), "blue": (0, 0, 255), "red": (255, 0, 0), "light_green": (100, 255, 100), "light_blue": (100, 100, 255), "light_red": (255, 100, 100),
               "even_lighter_red": (255, 125, 125)}

    start_button = Button(button_x, button_y, button_width, button_height, colours["green"], 0)  # XXX: wydaje mi sie, ze powinnismy gdzies tylko raz tworzyc te rzeczy w inicie
    settings_button = Button(button_x, button_y + button_offset, button_width, button_height, colours["blue"], 0)  # XXX: i przekazac jako argument zamiast tworzyc je co tick
    exit_button = Button(button_x, button_y + button_offset * 2, button_width, button_height, colours["red"], 0)

    if start_button.x_0 + start_button.width >= mouse[0] >= start_button.x_0 and start_button.y_0 <= mouse[1] <= start_button.y_0 + start_button.height or key_GREEN:
        start_button.colour = colours["light_green"]
        if click[0] == 1 or key_GREEN:
            GAME.game_init()
            menu_exit = check_click(0, GAME)
            return menu_exit
    start_button.draw(GAME.game_display)

    if settings_button.x_0 + settings_button.width >= mouse[0] >= settings_button.x_0 and settings_button.y_0 <= mouse[1] <= settings_button.y_0 + settings_button.height:
        settings_button.colour = colours["light_blue"]

        if click[0] == 1:  # XXX: ogolnie to wydaje mi sie, ze mozna by jakos w petli dla kazdego zrobic to sprawdzanie click zamiast przy kazdym osobno
            # pygame.draw.rect(GAME.game_display, (0, 0, 180), button2)  # TODO: taa bez kitu by mozna 100% ale mi sie nie chce
            menu_exit = check_click(2, GAME)
            return menu_exit
    settings_button.draw(GAME.game_display)

    if exit_button.x_0 + exit_button.width >= mouse[0] >= exit_button.x_0 and exit_button.y_0 <= mouse[1] <= exit_button.y_0 + button_height or key_RED:
        exit_button.colour = colours["light_red"]

        if click[0] == 1 or key_RED:
            exit_button.colour = colours["even_lighter_red"]
            exit_button.draw(GAME.game_display)
            menu_exit = check_click(1, GAME)
            return menu_exit
    exit_button.draw(GAME.game_display)


def check_click(choice, GAME):
    if choice == 0:
        GAME.game_exit = False
        return True
    elif choice == 1:
        GAME.game_exit = True
        return True
    elif choice == 2:
        settings.settings_loop(GAME)
        return False
