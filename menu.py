import pygame


def menu(game_display, GAME):

    menu_exit = False

    while not menu_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill((255, 255, 255))
        myfont = pygame.font.SysFont('monospace', 30)
        label = myfont.render("Pozaziemscy zaborcy", 1, (0, 0, 0))
        game_display.blit(label, (70, 150))
        menu_exit = check_mouse(game_display, GAME, menu_exit)

        pygame.display.update()
        pygame.time.Clock().tick(15)


def check_mouse(game_display, GAME, menu_exit):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 160 >= mouse[0] >= 60 and 250 <= mouse[1] <= 300:

        pygame.draw.rect(game_display, (120, 255, 120), (60, 250, 100, 50))

        if click[0] == 1:
            pygame.draw.rect(game_display, (120, 44, 23), (60, 250, 100, 50))
            menu_exit = (0, GAME, menu_exit)
            return menu_exit

    else:
        pygame.draw.rect(game_display, (0, 255, 0), (60, 250, 100, 50))

    if 450 >= mouse[0] >= 350 and 250 <= mouse[1] <= 300:

        pygame.draw.rect(game_display, (255, 60, 120), (350, 250, 100, 50))

        if click[0] == 1:
            pygame.draw.rect(game_display, (255, 120, 120), (350, 250, 100, 50))
            menu_exit = check_click(1, GAME, menu_exit)
            return menu_exit

    else:
        pygame.draw.rect(game_display, (255, 0, 0), (350, 250, 100, 50))


def check_click(choice, GAME, menu_exit):
    if choice == 0:
        GAME.game_exit = False
        return True
    elif choice == 1:
        GAME.game_exit = True
        return True