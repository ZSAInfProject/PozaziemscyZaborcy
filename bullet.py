from pygame import draw, image, transform
from math import sqrt
import os


class Bullet:
    velocity = 0
    x_pos = 0
    y_pos = 0
    exists = True
    player_start_x = 0
    direction = 0

    def __init__(self, pos_x, pos_y, force, half_entity_width, width, height):
        self.x_pos = pos_x + half_entity_width
        self.y_pos = pos_y
        self.velocity = force
        self.do_find_player_start_x = True
        self.width = width
        self.height = height
        self.bullet_model = transform.scale(__import__('resources').Resources.bullet_model, (self.width, self.height))

    def find_player_start_x(self, player):
        player = player
        p_x = player.s_x + player.width/2
        diff_y = player.s_y + player.width/2 - self.y_pos
        diff_x = player.s_x + player.width/2 - self.x_pos
        if self.velocity < 0:
            diff_xy = sqrt(diff_x**2 + diff_y**2)
            self.direction = -diff_x/(diff_xy)
            self.velocity = -diff_y/(diff_xy)

    def move(self):
        self.y_pos -= self.velocity
        self.x_pos -= self.direction  # self.sidemove(self.player_start_x)

    def draw(self, GAME):  # TODO: tych argumentow jest troche duzo...
        if self.do_find_player_start_x and self.velocity < 0:
            self.find_player_start_x(GAME.player)
            self.do_find_player_start_x = False
        self.move()
        for i, entity in enumerate(GAME.entities):  # bez range sie krzaczy przy usuwaniu entity (24 linia)
            # tutaj zmienia sie poziom trudnosci
            if entity.check_bullet(self):  # TODO: powinnismy rozrozniac width gracza i wroga, chyba?
                self.exists = False
                if self.velocity > 0:
                    del GAME.entities[i]
                    GAME.points += 10
                    break
                elif self.velocity < 0:
                    GAME.points -= 10
                    GAME.game_end = True
                    GAME.game_lost = True
                else:
                    print('this should never appear')
            elif self.y_pos <= 0 or self.y_pos >= GAME.screen_y:
                self.exists = False
        return self.exists, GAME.points
