import ship
import bullet
from pygame import draw


class EnemyShip(ship.Ship):

    def __init__(self, given_x=220, given_y=50):
        self.s_x = given_x
        self.s_y = given_y
        self.velocity = 1

    def check_walls(self):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == 470 and self.velocity > 0):
            return False
        else:
            return True

    def check_bullet(self, bull):
        if bull.y == self.s_y + 30 and (self.s_x <= bull.x <= self.s_x + 30):
            return True

    def check_player(self, player):
        if (self.s_y + 30 >= player.s_y >= self.s_y) and (self.s_x + 30 >= player.s_x >= self.s_x):
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, -2)

    def draw(self, gameDisplay):
        draw.rect(gameDisplay, (0, 0, 0), [self.s_x, self.s_y, 30, 30])
        if self.check_walls():
            self.s_x += self.velocity
        else:
            self.s_y += 20
            self.velocity *= -1
