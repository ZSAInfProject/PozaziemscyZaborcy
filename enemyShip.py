import ship
import bullet
from pygame import draw


class EnemyShip(ship.Ship):

    def __init__(self, given_x=220, given_y=50):
        self.s_x = given_x
        self.s_y = given_y
        self.velocity = 1

    def check_walls(self, screen_x, width):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == screen_x-width and self.velocity > 0):
            return False
        else:
            return True

    def check_bullet(self, bull, width):
        if bull.y == self.s_y + width and (self.s_x <= bull.x <= self.s_x + width):
            return True

    def check_player(self, player, width):
        if (self.s_y + width >= player.s_y >= self.s_y) and (self.s_x + width >= player.s_x >= self.s_x):
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, -2)

    def draw(self, gameDisplay, screen_x, width):
        draw.rect(gameDisplay, (0, 0, 0), [self.s_x, self.s_y, width, width])
        if self.check_walls(screen_x, width):
            self.s_x += self.velocity
        else:
            self.s_y += 20
            self.velocity *= -1
