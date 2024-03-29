import pygame
import player_ship
import enemy_field
from game_exit import GameExit
from resources import Resources


class Game:
    def game_init(self):
        resources = Resources()

        self.player = player_ship.PlayerShip(
            220, 0.9 * self.screen_y - self.width, resources.playership_model)
        self.enemies = []
        self.field = enemy_field.EnemyField(
            self.screen_x, resources.matej_model, resources.bullet_model)
        self.enemies = self.field.fill_with_enemies(self.enemies)

    def __init__(self):
        self.screen_x = 1024
        self.screen_y = 720
        self.width = 0

        self.game_display = pygame.display.set_mode(
            (self.screen_x, self.screen_y))

        pygame.display.set_caption('Pozaziemscy zaborcy')

        # Set music
        pygame.mixer.music.load('./sounds/codex.mp3')
        pygame.mixer.music.play(-1)

        # Set timer
        self.clock = pygame.time.Clock()
        self.tickrate = 120

        # Set font
        self.myfont = pygame.font.SysFont('monospace', 15)
        self.label = self.myfont.render("Points: 0", 1, (0, 0, 0))
        self.label_game_won = self.myfont.render("EZ WIN BOI", 1, (0, 0, 0))
        self.label_game_lost = self.myfont.render("Git gud n00b", 1, (0, 0, 0))

        # Set booleans
        self.game_exit = GameExit.FALSE
        self.game_end = False
        self.game_won = False
        self.game_lost = False

        # Set variables
        self.points = 0
        self.bullets = [None]
