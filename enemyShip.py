from pygame import draw
import ship
import bullet


class EnemyShip(ship.Ship):
    def __init__(self, given_width=30, given_x=220, given_y=50):
        self.s_x = given_x
        self.s_y = given_y
        self.width = given_width

    def check_player(self, player):  # wykraczy sie jesli kiedykolwiek gracz/enemy nie bedzie kwadratem
        if (self.s_x <= player.s_x <= self.s_x + self.width) or (self.s_x <= player.s_x + player.width <= self.s_x + self.width):
            if (self.s_y <= player.s_y <= self.s_y + self.width) or (self.s_y <= player.s_y + player.width <= self.s_y + self.width):
                # if (self.s_y + self.width >= player.s_y >= self.s_y) and (self.s_x + self.width >= player.s_x >= self.s_x):  # patrzy tylko na 1 wspolrzedna gracza
                return True

    def shoot(self):
        return bullet.Bullet(self.s_x, -2)

    def draw(self, gameDisplay):
        draw.rect(gameDisplay, (0, 0, 0), [self.s_x, self.s_y, self.width, self.width])

    def move(self, velocity, addY):
        self.s_x += velocity
        self.s_y += addY
