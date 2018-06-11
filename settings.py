import pygame
import button
import enum
from collections import OrderedDict

pygame.init()

class Resolution(enum.Enum):
    HD = (1280, 720)
    WXGA = (1366, 768)
    HDplus = (1600, 900)
    FHD = (1920, 1080)


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


def find_resolution_pos(mouse, button_x, button_width):
    res = OrderedDict()
    amount = len(Resolution) - 1
    for i, resolution in enumerate(Resolution):
        res[resolution.value] = button_x + (i/amount)*button_width
    return res


def initialize_buttons(GAME):
    button_width, button_height = 400, 60
    button_x, button_y = GAME.screen_x-button_width, GAME.screen_y-button_height

    resolution_button = button.Button(button_x*0.5, button_y*0.5, button_width, button_height, (0, 255, 0), 0)
    button_outline = button.Button(button_x*0.5, button_y*0.5, button_width, button_height, (0, 0, 0), 3)
    return resolution_button, button_outline


def update_resolution_button(GAME, resolution_button, resolutions_distance, mouse):
    temp = float("Inf")
    res_temp = 0
    for i, resolution in enumerate(resolutions_distance.values()):
        if abs(resolution - mouse[0]) < temp:
            temp = abs(resolution - mouse[0])
            res_temp = resolution - resolution_button.x_0
            chosen_resolution = i
    resolution_button.width = res_temp
    return chosen_resolution


def check_mouse(GAME, settings_exit, resolution_button, button_outline):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    button_outline.draw(GAME.game_display)
    resolution_button.draw(GAME.game_display)
    # button_offset = button_height + 30

    resolutions_distance = find_resolution_pos(mouse, button_outline.x_0, button_outline.width)

    if button_outline.x_0 + button_outline.width >= mouse[0] >= button_outline.x_0 and button_outline.y_0 <= mouse[1] <= button_outline.y_0 + button_outline.height:
        mouse = pygame.mouse.get_pos()
        resolution_button.colour = (60, 255, 60)

        if click[0] == 1:
            chosen_resolution = update_resolution_button(GAME, resolution_button, resolutions_distance, mouse)
            change_resolution(GAME, chosen_resolution)
            return (False)  # True

        else:
            return(False)
    resolution_button.colour = (0, 255, 0)
    return (False)


def change_resolution(GAME, chosen_resolution):

    for i, res in enumerate(Resolution):
        if i == chosen_resolution:
            chosen_size = res.value

    GAME.game_display = pygame.display.set_mode(chosen_size)

