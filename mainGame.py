import pygame
import playerShip
import enemyField
from game import Game

pygame.init()
game = Game()


def game_loop():
    while not game.gameExit:

        # Event-catching loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game.entities[0].addVelocity(-1)
                if event.key == pygame.K_d:
                    game.entities[0].addVelocity(1)
                if event.key == pygame.K_RETURN and game.bullets[0] is None:
                    game.bullets[0] = game.entities[0].shoot()
                if event.key == pygame.K_q:
                    game.gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    game.entities[0].addVelocity(1)
                if event.key == pygame.K_d:
                    game.entities[0].addVelocity(-1)

        # Fill screen with white color
        game.gameDisplay.fill((255, 255, 255))

        # Draw player
        game.entities[0].draw(game.gameDisplay, game.screen_x)

        # Draw field
        game.field.draw(game.screen_x, game.gameDisplay, game.entities)

        # Draw enemies
        for enemy in range(1, len(game.entities)):
            game.entities[enemy].draw(game.gameDisplay)
            if game.entities[enemy].check_player(game.entities[0]):
                del game.entities[enemy]
                game.points -= 10
                break

        # Check bullet condition
        for i, bullet in enumerate(game.bullets):
            if bullet is not None:
                bulletExists, game.points = bullet.draw(game.gameDisplay, game.screen_y, game.entities, game.width, game.points)
                if not bulletExists:
                    if i >= 1:
                        del game.bullets[i]
                    else:
                        game.bullets[i] = None

        # Update display, maintain stable framerate
        label = game.myfont.render("Points: " + str(game.points), 1, (0, 0, 0))
        game.gameDisplay.blit(label, (10, 10))
        pygame.display.update()
        game.clock.tick(120)
