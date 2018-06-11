import pygame
import button


pygame.init()


def settings_loop(GAME):

    settings_exit = False
    resolutions_button, button_outline = initialize_buttons(GAME)

    while not settings_exit:

        GAME.game_display.fill((255, 255, 255))
        settings_exit = check_mouse(GAME, settings_exit, resolutions_button, button_outline)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    settings_exit = True


def find_resolution_pos(mouse, resolutions, button_x, button_width):
    res = {}
    amount = len(resolutions) - 1
    for i, resolution in enumerate(resolutions):
        res[resolution] = button_x + (i/amount)*button_width
    return res


def initialize_buttons(GAME):
    button_width, button_height = 400, 60
    button_x, button_y = GAME.screen_x-button_width, GAME.screen_y-button_height

    resolution_button = button.Button(button_x*0.5, button_y*0.5, button_width, button_height, (0, 255, 0), 0)
    button_outline = button.Button(button_x*0.5, button_y*0.5, button_width, button_height, (0, 0, 0), 3)
    return resolution_button, button_outline


def update_resolution_button(GAME, resolution_button, resolutions, mouse):
    temp = float("Inf")
    res_temp = 0
    for resolution in resolutions.values():
        if abs(resolution - mouse[0]) < temp:
            temp = abs(resolution - mouse[0])
            res_temp = resolution - resolution_button.x_0
    resolution_button.width = res_temp
    return 0


def check_mouse(GAME, settings_exit, resolution_button, button_outline):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    resolutions = ['720', '768', '900', '1080']

    button_outline.draw(GAME.game_display)
    resolution_button.draw(GAME.game_display)
    # button_offset = button_height + 30

    resolutions = find_resolution_pos(mouse, resolutions, button_outline.x_0, button_outline.width)

    if button_outline.x_0 + button_outline.width >= mouse[0] >= button_outline.x_0 and button_outline.y_0 <= mouse[1] <= button_outline.y_0 + button_outline.height:
        mouse = pygame.mouse.get_pos()
        resolution_button.colour = (60, 255, 60)

        if click[0] == 1:
            update_resolution_button(GAME, resolution_button, resolutions, mouse)
            #settings_exit = check_click(0, GAME)
            return (False)  # True

        else:
            return(False)
    resolution_button.colour = (0, 255, 0)
    return (False)


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
