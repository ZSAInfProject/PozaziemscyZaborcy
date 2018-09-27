import pygame
import ship
import bullet
import os


class PlayerShip(ship.Ship):
    #FIXME skalowanie width i height daje mi raka
    def __init__(self, given_x, given_y, playership_model, bullet_model):
        self.s_x = given_x
        self.s_y = given_y
        self.width = int(674/10)
        self.height = int(1507/10)
        self.player_model = pygame.transform.scale(playership_model, (self.width, self.height))  # (self.width, self.width))
        self.bullet_model = bullet_model

    #FIXME no ten if to chyba troszku długi
    def check_walls(self, screen_x):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == screen_x - self.width and self.velocity > 0):
            return False
        else:
            return True

    #FIXME pojebało z tym pociskiem chyba
    def shoot(self):
        return bullet.Bullet(self.s_x, self.s_y - self.bullet_height, 6, self.width * 0.5, self.bullet_width, self.bullet_height, self.bullet_model)

    #FIXME ładne
    def touched_wall(self, screen_x):
        if self.check_walls(screen_x):
            self.s_x += self.velocity
        return True
