import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Pozaziemscy zaborcy')

x = 255

y_rect = 450
x_rect = 100
velocity = 0

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                velocity -= 0.2
            if event.key == pygame.K_d:
                velocity += 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                velocity = 0
            if event.key == pygame.K_d:
                velocity = 0

    x_rect += velocity

    gameDisplay.fill((x, x, x))
    pygame.draw.rect(gameDisplay, (0, 0, 0), [x_rect, y_rect, 30, 30])
    pygame.display.update()


pygame.quit()
quit()