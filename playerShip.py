import ship
import bullet
from pygame import draw


class PlayerShip(ship.Ship):
    def __init__(self, given_x=220, given_y=450):
        self.s_x = given_x
        self.s_y = given_y

    def check_walls(self, screen_x):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == screen_x - 30 and self.velocity > 0):
            return False
        else:
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, 2)

    def draw(self, gameDisplay, screen_x, width):
        draw.rect(gameDisplay, (0, 0, 0), [self.s_x, self.s_y, width, width])
        if self.check_walls(screen_x):
            self.s_x += self.velocity
        return True
