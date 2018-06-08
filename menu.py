import pygame
import settings

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

    button1 = (button_x, button_y, button_width, button_height)
    button2 = (button_x, button_y + button_offset, button_width, button_height)
    button3 = (button_x, button_y + 2*button_offset, button_width, button_height)

    if button_x + button_width >= mouse[0] >= button_x and button_y <= mouse[1] <= button_y + button_height or key_GREEN:

        pygame.draw.rect(GAME.game_display, (120, 255, 120), button1)

        if click[0] == 1 or key_GREEN:
            pygame.draw.rect(GAME.game_display, (120, 44, 23), button1)
            menu_exit = check_click(0, GAME)
            return menu_exit

    else:
        pygame.draw.rect(GAME.game_display, (0, 255, 0), button1)

    if button_x + button_width >= mouse[0] >= button_x and button_y + button_offset <= mouse[1] <= button_y + button_offset + button_height:

        pygame.draw.rect(GAME.game_display, (200, 200, 200), button2)

        if click[0] == 1:
            pygame.draw.rect(GAME.game_display, (0, 0, 180), button2)
            menu_exit = check_click(2, GAME)
            return menu_exit

    else:
        pygame.draw.rect(GAME.game_display, (0, 0, 255), button2)

    if button_x + button_width >= mouse[0] >= button_x and button_y + 2*button_offset <= mouse[1] <= button_y + 2*button_offset + button_height or key_RED:

        pygame.draw.rect(GAME.game_display, (255, 60, 120), button3)

        if click[0] == 1 or key_RED:
            pygame.draw.rect(GAME.game_display, (255, 120, 120), button3)
            menu_exit = check_click(1, GAME)
            return menu_exit

    else:
        pygame.draw.rect(GAME.game_display, (255, 0, 0), button3)

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
