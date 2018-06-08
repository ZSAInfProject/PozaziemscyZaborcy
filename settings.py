import pygame

pygame.init()

def settings_loop(GAME):

    settings_exit = False

    while not settings_exit:

        GAME.game_display.fill((255, 255, 255))
        settings_exit = resolutions(GAME, settings_exit)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    settings_exit = True

def resolutions(GAME, settings_exit):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    button_width = 400
    button_x = (1920 - button_width) * 0.5
    button_height = 60
    button_y = (1080 - button_height) * 0.5
    #button_offset = button_height + 30

    button1 = (button_x, button_y, button_width, button_height)
    #button2 = (button_x, button_y + button_offset, button_width, button_height)

    pygame.draw.rect(GAME.game_display, (120, 255, 120), button1)

    if button_x + button_width >= mouse[0] >= button_x and button_y <= mouse[1] <= button_y + button_height:
        mouse = pygame.mouse.get_pos()

        if click[0] == 1:
            pygame.draw.rect(GAME.game_display, (120, 44, 23), button1)
            settings_exit = check_click(0, GAME)
            return True

        else:
            pygame.draw.rect(GAME.game_display, (0, 255, 0), button1)
        
    return False


def check_click(choice, GAME):
    if choice == 0:
        screen_size = (1366, 768)
        is_fullscreen = True
        check_flags(GAME, screen_size, is_fullscreen)
        return False
    elif choice == 1:
        screen_size = (1366, 768)
        is_fullscreen = False
        check_flags(GAME, screen_size, is_fullscreen)
        return False

def check_flags(GAME, screen_size, is_fullscreen):
    if is_fullscreen:
        GAME.game_display = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    else:
        GAME.game_display = pygame.display.set_mode(screen_size)