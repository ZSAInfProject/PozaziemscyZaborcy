from math import sqrt
from pygame import draw, transform, image
import ship
import bullet
import os
import resources


class EnemyShip(ship.Ship):

    def __init__(self, given_x, given_y, given_width, model, bullet_model):
        self.s_x = given_x
        self.s_y = given_y
        self.width = given_width
        self.height = self.width
        self.is_enemy = True
        self.enemy_model = transform.scale(model, (self.width, self.height))  # (self.width, self.width))
        self.bullet_model = bullet_model

    def check_player(self, player):  # wykraczy sie jesli kiedykolwiek gracz/enemy nie bedzie kwadratem
        if ((self.s_x <= player.s_x <= self.s_x + self.width) or (self.s_x <= player.s_x + player.width <= self.s_x + self.width)) and \
                ((self.s_y <= player.s_y <= self.s_y + self.width) or (self.s_y <= player.s_y + player.width <= self.s_y + self.width)):
            return True
        return False

    def shoot(self):
        return bullet.Bullet(self.s_x, self.s_y + self.width, -4545, self.width * 0.1, self.bullet_width - 10, self.bullet_height - 80, self.bullet_model)

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

    def move(self, velocity, add_y):
        self.s_x += velocity
        self.s_y += add_y
