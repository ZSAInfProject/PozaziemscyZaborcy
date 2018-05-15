import pygame
import player
import bullet

pygame.init()

gameDisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Pozaziemscy zaborcy')

x = 255

gameExit = False
bulletDisplay = False

player = player.Player()

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move(-0.2)
            if event.key == pygame.K_d:
                player.move(0.2)
            if event.key == pygame.K_o:
                bul = bullet.Bullet(player.p_x)
                bulletDisplay = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.move(0)
            if event.key == pygame.K_d:
                player.move(0)

    if player.check_walls():
        player.p_x += player.velocity

    gameDisplay.fill((x, x, x))
    pygame.draw.rect(gameDisplay, (0, 0, 0), [player.p_x, player.p_y, 30, 30])

    if bulletDisplay:
        bul.move()
        pygame.draw.rect(gameDisplay, (0, 0, 0), [bul.x, bul.y, 2, 10])

    pygame.display.update()


pygame.quit()
quit()