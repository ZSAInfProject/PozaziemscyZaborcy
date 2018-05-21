#!/usr/bin/python3

import pygame
import playerShip
import enemyShip
import enemyField


def main():
    # Initialize pygame module
    pygame.init()

    screen_x = 500
    screen_y = 500

    width = 30

    # Set basic elements
    gameDisplay = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Pozaziemscy zaborcy')

    # Set music
    pygame.mixer.music.load('./sounds/codex.mp3')
    pygame.mixer.music.play()

    # Set timer
    clock = pygame.time.Clock()

    # Set font
    myfont = pygame.font.SysFont('monospace', 15)
    label = myfont.render("Points: 0", 1, (0, 0, 0))

    # Set booleans
    gameExit = False

    # Set variables
    points = 0
    bullets = [None]

    # Set starting objects
    entities = []
    entities.append(playerShip.PlayerShip(width))
    # entities.append(enemyShip.EnemyShip(width))
    eF = enemyField.EnemyField(gameDisplay, screen_x, width)
    entities = eF.fillWithEnemies(entities)
    for entity in entities:
        print(entity.s_x)

    # Main game loop
    while not gameExit:

        # Event-catching loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    entities[0].addVelocity(-1)
                if event.key == pygame.K_d:
                    entities[0].addVelocity(1)
                if event.key == pygame.K_RETURN and bullets[0] is None:
                    bullets[0] = entities[0].shoot()
                if event.key == pygame.K_q:
                    gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    entities[0].addVelocity(1)
                if event.key == pygame.K_d:
                    entities[0].addVelocity(-1)

        # Fill screen with white color
        gameDisplay.fill((255, 255, 255))

        # Draw player
        entities[0].draw(gameDisplay, screen_x)

        # Draw ememies
        for enemy in range(1, len(entities)):
            entities[enemy].draw(gameDisplay, screen_x)
            if entities[enemy].check_player(entities[0]):
                del entities[enemy]
                points -= 10

        # Check bullet condition
        for bullet in range(len(bullets)):
            if bullets[bullet] is not None:
                bulletExists, points = bullets[bullet].draw(gameDisplay, screen_y, entities, width, points)
                if not bulletExists:
                    if bullet >= 1:
                        del bullets[bullet]
                    else:
                        bullets[bullet] = None

        # Update display, maintain stable framerate
        label = myfont.render("Points: " + str(points), 1, (0, 0, 0))
        gameDisplay.blit(label, (10, 10))
        pygame.display.update()
        clock.tick(120)

    # Exit game
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
