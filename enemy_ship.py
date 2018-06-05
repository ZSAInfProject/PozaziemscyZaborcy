from math import sqrt
from pygame import draw
import ship
import bullet


class EnemyShip(ship.Ship):

    def __init__(self, given_x, given_y, given_width):
        self.s_x = given_x
        self.s_y = given_y
        self.width = given_width

    def check_player(self, player):  # wykraczy sie jesli kiedykolwiek gracz/enemy nie bedzie kwadratem
        if ((self.s_x <= player.s_x <= self.s_x + self.width) or (self.s_x <= player.s_x + player.width <= self.s_x + self.width)) and \
                ((self.s_y <= player.s_y <= self.s_y + self.width) or (self.s_y <= player.s_y + player.width <= self.s_y + self.width)):
            return True
        return False

    def shoot(self):
        return bullet.Bullet(self.s_x, self.s_y + self.width, -6, self.width * 0.5)

    def distance_from_player(self, player_x, player_y, player_width):  # TODO: player width, length
        mid_x = self.s_x + self.width/2
        #mid_y = self.s_y + self.width/2
        player_mid_x = player_x + player_width/2
        #player_mid_y = player_y + player_width/2
        #distance = sqrt((mid_x - player_mid_x)**2 + (mid_y - player_mid_y)**2)
        distance = mid_x - player_mid_x
        if distance < 0:
            distance = -distance
        return distance

    def draw(self, game_display):
        draw.rect(game_display, (0, 0, 0), [self.s_x, self.s_y, self.width, self.width])

    def move(self, velocity, add_y):
        self.s_x += velocity
        self.s_y += add_y
