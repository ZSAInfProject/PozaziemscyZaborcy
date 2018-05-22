import pygame
import playerShip
import enemyField
from game import Game

pygame.init()
GAME = Game()


def event_catch():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME.gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                GAME.entities[0].addVelocity(-1)
            if event.key == pygame.K_d:
                GAME.entities[0].addVelocity(1)
            if event.key == pygame.K_RETURN and GAME.bullets[0] is None:
                GAME.bullets[0] = GAME.entities[0].shoot()
            if event.key == pygame.K_q:
                GAME.gameExit = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                GAME.entities[0].addVelocity(1)
            if event.key == pygame.K_d:
                GAME.entities[0].addVelocity(-1)


def draw_enemies():
    for enemy in range(1, len(GAME.entities)):
        GAME.entities[enemy].draw(GAME.gameDisplay)
        if GAME.entities[enemy].check_player(GAME.entities[0]):
            del GAME.entities[enemy]
            GAME.points -= 10
            break


def check_bullet_condition():
    for i, bullet in enumerate(GAME.bullets):
        if bullet is not None:
            bulletExists, GAME.points = bullet.draw(GAME.gameDisplay, GAME.screen_y, GAME.entities, GAME.width, GAME.points)
            if not bulletExists:
                if i >= 1:
                    del GAME.bullets[i]
                else:
                    GAME.bullets[i] = None


def game_loop():
    while not GAME.gameExit:

        # Event-catching loop
        event_catch()

        # Fill screen with white color
        GAME.gameDisplay.fill((255, 255, 255))

        # Draw player
        GAME.entities[0].draw(GAME.gameDisplay, GAME.screen_x)

        # Draw field
        GAME.field.draw(GAME.screen_x, GAME.gameDisplay, GAME.entities)

        # Draw enemies
        draw_enemies()

        # Check bullet condition
        check_bullet_condition()

        # Update display, maintain stable framerate
        label = GAME.myfont.render("Points: " + str(GAME.points), 1, (0, 0, 0))
        GAME.gameDisplay.blit(label, (10, 10))
        pygame.display.update()
        GAME.clock.tick(120)
