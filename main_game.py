import pygame
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
            if event.key == pygame.K_RETURN and GAME.bullets[0] is None:
                GAME.bullets[0] = GAME.entities[0].shoot()
            if event.key == pygame.K_q:
                GAME.game_exit = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                GAME.entities[0].add_velocity(1)
            if event.key == pygame.K_d:
                GAME.entities[0].add_velocity(-1)


def draw_enemies():
    for enemy in range(1, len(GAME.entities)):
        GAME.entities[enemy].draw(GAME.game_display)
        if GAME.entities[enemy].check_player(GAME.entities[0]):
            del GAME.entities[enemy]
            GAME.points -= 10
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


def game_loop():
    while not GAME.game_exit:

        # Event-catching loop
        event_catch()

        # Fill screen with white color
        GAME.game_display.fill((255, 255, 255))

        # Draw player
        GAME.entities[0].draw(GAME.game_display, GAME.screen_x)

        # Draw field
        GAME.field.draw(GAME.screen_x, GAME.game_display, GAME.entities)

        # Draw enemies
        draw_enemies()

        # Check bullet condition
        check_bullet_condition()

        # Update display, maintain stable framerate
        label = GAME.myfont.render("Points: " + str(GAME.points), 1, (0, 0, 0))
        GAME.game_display.blit(label, (10, 10))
        pygame.display.update()
        GAME.clock.tick(120)
