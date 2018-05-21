from pygame import draw
import ship
import bullet


class EnemyShip(ship.Ship):
    def __init__(self, given_width=30, given_x=220, given_y=50):
        self.s_x = given_x
        self.s_y = given_y
        self.width = given_width
        self.velocity = 1

    def check_walls(self, screen_x):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == screen_x-self.width and self.velocity > 0):
            return False
        else:
            return True

    def check_player(self, player):
        if (self.s_y + self.width >= player.s_y >= self.s_y) and (self.s_x + self.width >= player.s_x >= self.s_x):
            return True

    def shoot(self):
        return bullet.Bullet(self.s_x, -2)

    def draw(self, gameDisplay, screen_x):
        draw.rect(gameDisplay, (0, 0, 0), [self.s_x, self.s_y, self.width, self.width])
        if self.check_walls(screen_x):
            self.s_x += self.velocity
        else:
            self.s_y += 20
            self.velocity *= -1
