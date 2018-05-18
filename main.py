import pygame
import playerShip
import enemyShip


def main():
    # Initialize pygame module
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    pygame.mixer.init()

    screen_x = 500
    screen_y = 500

    width = 30

    # Set basic elements
    gameDisplay = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Pozaziemscy zaborcy')
    myfont = pygame.font.SysFont('monospace', 15)
    Music = pygame.mixer.Sound('./sounds/codex.wav')

    # Set timer
    clock = pygame.time.Clock()

    # Set font
    label = myfont.render("Points: 0", 1, (0, 0, 0))

    # Set booleans
    gameExit = False
    bulletDisplay = False
    showEnemy = True

    # Set variables
    points = 0

    # Set starting objects
    entities = []
    entities.append(playerShip.PlayerShip())
    entities.append(enemyShip.EnemyShip())

    # Main game loop
    while not gameExit:

        Music.play()

        # Event-catching loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    entities[0].addVelocity(-1)
                if event.key == pygame.K_d:
                    entities[0].addVelocity(1)
                if event.key == pygame.K_RETURN and not bulletDisplay:
                    bul = entities[0].shoot()
                    bulletDisplay = True
                if event.key == pygame.K_q:
                    gameExit = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    entities[0].addVelocity(1)
                if event.key == pygame.K_d:
                    entities[0].addVelocity(-1)

        # Fill screen with white color
        gameDisplay.fill((255, 255, 255))

        # Check player condition
        entities[0].draw(gameDisplay, screen_x, width)
        # Check enemy condition
        if showEnemy:
            entities[1].draw(gameDisplay, screen_x, width)
            if entities[1].check_player(entities[0], width):
                del entities[1]
                showEnemy = False
                points -= 10

        # Check bullet condition
        if bulletDisplay:
            bul.move()
            pygame.draw.rect(gameDisplay, (0, 0, 0), [bul.x, bul.y, 2, 10])
            if bul.y == 0:
                del bul
                bulletDisplay = False
            elif showEnemy:
                if entities[1].check_bullet(bul, width):
                    del bul
                    del entities[1]
                    bulletDisplay = False
                    showEnemy = False
                    points += 10

        # Update display, maintain stable framerate
        label = myfont.render("Points: " + str(points), 1, (0, 0, 0))
        gameDisplay.blit(label, (10, 10))
        pygame.display.update()
        clock.tick(120)
        clock.get_fps()

    # Exit game
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
