import pygame
import player_ship
import enemy_field


class Game:
    def __init__(self):
        self.screen_x = 500
        self.screen_y = 500
        self.width = 30

        self.game_display = pygame.display.set_mode((self.screen_x, self.screen_y))
        pygame.display.set_caption('Pozaziemscy zaborcy')

        # Set music
        pygame.mixer.music.load('./sounds/codex.mp3')
        pygame.mixer.music.play(-1)

        # Set timer
        self.clock = pygame.time.Clock()

        # Set font
        self.myfont = pygame.font.SysFont('monospace', 15)
        self.label = self.myfont.render("Points: 0", 1, (0, 0, 0))
        self.label_game_won = self.myfont.render("EZ WIN BOI", 1, (0, 0, 0))
        self.label_game_lost = self.myfont.render("Git gud n00b", 1, (0, 0, 0))

        # Set booleans
        self.game_exit = False
        self.game_end = False
        self.game_won = False
        self.game_lost = False

        # Set variables
        self.points = 0
        self.bullets = [None]

        # Set starting objects
        self.entities = []
        self.entities.append(player_ship.PlayerShip(self.game_display, self.width))
        self.field = enemy_field.EnemyField(self.screen_x, self.width)
        self.entities = self.field.fill_with_enemies(self.entities)
