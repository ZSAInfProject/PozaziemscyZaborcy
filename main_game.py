import pygame
import menu
from game import Game

pygame.init()
GAME = Game()


def event_catch():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME.game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                GAME.entities[0].add_velocity(-1)
            if event.key == pygame.K_d:
                GAME.entities[0].add_velocity(1)
            if event.key == pygame.K_RETURN and GAME.bullets[0] is None and not GAME.game_end:
                GAME.bullets[0] = GAME.entities[0].shoot()
                wewe = GAME.field.find_shooter(GAME.entities)
                GAME.bullets.append(GAME.entities[wewe].shoot())
            if event.key == pygame.K_q:
                GAME.game_exit = True
        if event.type == pygame.KEYUP and not GAME.game_end:
            if event.key == pygame.K_a:
                GAME.entities[0].add_velocity(1)
            if event.key == pygame.K_d:
                GAME.entities[0].add_velocity(-1)


def draw_enemies():  # pytanie, czy rysowac powinne sie same, czy pole powinno ich rysowac?
    for enemy in range(1, len(GAME.entities)):
        GAME.entities[enemy].draw(GAME.game_display)
        if GAME.entities[enemy].check_player(GAME.entities[0]):
            GAME.points = 0
            GAME.game_end = True
            GAME.game_lost = True
            del GAME.entities
            del GAME.field
            break


def check_bullet_condition():
    for i, bullet in enumerate(GAME.bullets):
        if bullet is not None:
            bullet_exists, GAME.points = bullet.draw(GAME.game_display, GAME.screen_y, GAME.entities, GAME.width, GAME.points)
            if not bullet_exists:
                if i >= 1:
                    del GAME.bullets[i]
                else:
                    GAME.bullets[i] = None


def check_field_existence():
    if not GAME.field.exists:
        del GAME.field
        GAME.game_end = True
        GAME.game_won = True


def draw_game_won():
    if GAME.game_won:
        GAME.game_display.blit(GAME.label_game_won, (200, 220))
    else:
        check_field_existence()


def draw_field():
    if not GAME.game_won:
        GAME.field.draw(GAME.screen_x, GAME.game_display, GAME.entities)


def draw_game_lost():
    if GAME.game_lost:
        GAME.game_display.blit(GAME.label_game_lost, (200, 220))


def check_game_status():
    if GAME.game_end:
        if GAME.game_won:
            draw_game_won()
        else:
            draw_game_lost()
    else:
        # Draw field
        draw_field()
        draw_game_won()

        # Draw player
        GAME.entities[0].draw(GAME.game_display, GAME.screen_x)

        # Draw enemies
        draw_enemies()

        # Check bullet condition
        check_bullet_condition()


def game_loop():

    menu.menu(GAME.game_display, GAME)

    while not GAME.game_exit:

        # Event-catching loop
        event_catch()

        # Fill screen with white color
        GAME.game_display.fill((255, 255, 255))

        # Status of the game (win/lose/in progress)
        check_game_status()

        # Update display, maintain stable framerate
        label = GAME.myfont.render("Points: " + str(GAME.points), 1, (0, 0, 0))
        GAME.game_display.blit(label, (10, 10))
        pygame.display.update()
        GAME.clock.tick(120)
