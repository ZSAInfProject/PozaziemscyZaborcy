import pygame
import playerShip
import enemyField


class Game:
    def __init__(self):
        self.screen_x = 500
        self.screen_y = 500
        self.width = 30

        self.gameDisplay = pygame.display.set_mode((self.screen_x, self.screen_y))
        pygame.display.set_caption('Pozaziemscy zaborcy')

        # Set music
        pygame.mixer.music.load('./sounds/codex.mp3')
        pygame.mixer.music.play()

        # Set timer
        self.clock = pygame.time.Clock()

        # Set font
        self.myfont = pygame.font.SysFont('monospace', 15)
        self.label = self.myfont.render("Points: 0", 1, (0, 0, 0))

        # Set booleans
        self.gameExit = False

        # Set variables
        self.points = 0
        self.bullets = [None]

        # Set starting objects
        self.entities = []
        self.entities.append(playerShip.PlayerShip(self.width))
        self.field = enemyField.EnemyField(self.screen_x, self.width)
        self.entities = self.field.fillWithEnemies(self.entities)