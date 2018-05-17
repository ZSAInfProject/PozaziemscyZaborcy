import pygame
import playerShip
import bullet
import enemyShip


def main():
    # Initialize pygame module
    pygame.init()

    # Set basic elements
    gameDisplay = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Pozaziemscy zaborcy')
    myfont = pygame.font.SysFont('monospace', 15)

    # Set timer
    clock = pygame.time.Clock()

    # Set font
    label = myfont.render("Points: 0", 1, (0, 0, 0))

    # Set booleans
    gameExit = False
    bulletDisplay = False
    showEnemy = True
    showPlayer = True

    # Set variables
    points = 0

    # Set starting objects
    player = playerShip.PlayerShip()
    enemy = enemyShip.EnemyShip()

    # Main game loop
    while not gameExit:
        # Event-catching loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.addVelocity(-1)
                if event.key == pygame.K_d:
                    player.addVelocity(1)
                if event.key == pygame.K_o and bulletDisplay == False:
                    bul = bullet.Bullet(player.s_x)
                    bulletDisplay = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.addVelocity(1)
                if event.key == pygame.K_d:
                    player.addVelocity(-1)

        # Fill screen with white color
        gameDisplay.fill((255, 255, 255))

        # Check player condition
        if showPlayer:
            if player.check_walls():
                player.s_x += player.velocity
            pygame.draw.rect(gameDisplay, (0, 0, 0), [player.s_x, player.s_y, 30, 30])

        # Check enemy condition
        if showEnemy:
            pygame.draw.rect(gameDisplay, (0, 0, 0), [enemy.s_x, enemy.s_y, 30, 30])
            if enemy.check_walls():
                enemy.s_x += enemy.velocity
            else:
                enemy.s_y += 20
                enemy.velocity *= -1
            if enemy.check_player(player):
                del player
                del enemy
                showEnemy = False
                showPlayer = False
                points -= 10

        # Check bullet condition
        if bulletDisplay:
            bul.move()
            pygame.draw.rect(gameDisplay, (0, 0, 0), [bul.x, bul.y, 2, 10])
            if bul.y == 0:
                del bul
                bulletDisplay = False
            elif showEnemy == True:
                if enemy.check_bullet(bul):
                    del bul
                    del enemy
                    bulletDisplay = False
                    showEnemy = False
                    points += 10
                    continue

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
