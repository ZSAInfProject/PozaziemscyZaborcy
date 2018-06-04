from pygame import draw
import ship
import bullet


class PlayerShip(ship.Ship):
    def __init__(self, given_width=30, given_x=950, given_y=850):
        self.s_x = given_x
        self.s_y = given_y
        self.width = given_width

    def check_walls(self, screen_x):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == screen_x - 30 and self.velocity > 0):
            return False
        else:
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, self.s_y, 4)

    def draw(self, game_display, screen_x):
        draw.rect(game_display, (0, 0, 0), [self.s_x, self.s_y, self.width, self.width])
        if self.check_walls(screen_x):
            self.s_x += self.velocity
        return True
