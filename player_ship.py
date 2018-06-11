import pygame
import ship
import bullet
import os

class PlayerShip(ship.Ship):
    def __init__(self, game_display, given_width=30, given_x=220, given_y=450):
        self.s_x = given_x
        self.s_y = given_y - 100
        self.width = given_width
        self.obrazek = pygame.image.load(os.path.join('./textures/', 'playership.png'))
        self.player_model = pygame.transform.scale(self.obrazek, (50, 100))
        #self.oteksturowane = game_display.blit(self.obrazek, [self.s_x, self.s_y, self.width, self.width])

    def check_walls(self, screen_x):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == screen_x - self.width and self.velocity > 0):
            return False
        else:
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, self.s_y, 6, self.width * 0.5)

    def draw(self, game_display, screen_x):
        game_display.blit(self.player_model, [self.s_x, self.s_y, self.width, self.width])
        if self.check_walls(screen_x):
            self.s_x += self.velocity
        return True
