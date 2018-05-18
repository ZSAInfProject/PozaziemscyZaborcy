import ship
import bullet
from pygame import draw

# def show_player(player):
#   if player.check_walls():
#      player.s_x += player.velocity
# return True


class PlayerShip(ship.Ship):
    def __init__(self, given_x=220, given_y=450):
        self.s_x = given_x
        self.s_y = given_y

    def check_walls(self):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == 470 and self.velocity > 0):
            return False
        else:
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, 2)

    def draw(self, gameDisplay):
        draw.rect(gameDisplay, (0, 0, 0), [self.s_x, self.s_y, 30, 30])
        if self.check_walls():
            self.s_x += self.velocity
        return True
