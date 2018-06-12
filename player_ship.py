import pygame
import ship
import bullet
import os


class PlayerShip(ship.Ship):
    def __init__(self, given_x=220, given_y=450):
        self.s_x = given_x
        self.s_y = given_y
        self.width = int(674/10)
        self.height = int(1507/10)
        self.obrazek = pygame.image.load(os.path.join('./textures/', 'playership.png'))
        self.player_model = pygame.transform.scale(self.obrazek, (self.width, self.height))  # (self.width, self.width))

    def check_walls(self, screen_x):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == screen_x - self.width and self.velocity > 0):
            return False
        else:
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, self.s_y - self.bullet_height, 6, self.width * 0.5, self.bullet_width, self.bullet_height)

    def draw(self, game_display, screen_x):
        pygame.draw.rect(game_display, (0, 0, 0), [self.s_x, self.s_y, self.width, self.height])
        game_display.blit(self.player_model, [self.s_x, self.s_y, self.width, self.width])
        if self.check_walls(screen_x):
            self.s_x += self.velocity
        return True
