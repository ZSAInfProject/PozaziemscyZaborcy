from pygame import draw, image, transform
from math import sqrt
import os
import resources


class Bullet:
    velocity = 0
    x_pos = 0
    y_pos = 0
    #FIXME Czy nie dałoby rady ominąć tego bool'a? (Bo kiedy pocisk istnieje to po prostu jest,
    # a w przeciwnym wypadku zrobić pop() z tablicy albo ustawić na None (lepsze pop))
    exists = True
    #FIXME chyba słaba nazwa bo to chyba ustawia się i dla gracza i przeciwnika c nie?
    player_start_x = 0
    #FIXME To może powinien być jakiś bool albo enum
    direction = 0

    #FIXME Trochę nawalone ale jakoś potrzebne, więc nwm
    def __init__(self, pos_x, pos_y, force, half_entity_width, width, height, model):
        self.x_pos = pos_x + half_entity_width
        self.y_pos = pos_y
        self.velocity = force
        self.do_find_player_start_x = True
        self.width = width
        self.height = height
        self.bullet_model = transform.scale(model, (self.width, self.height))

    #FIXME ahh... ten player jako entities[0], piękna sprawa
    def find_player_start_x(self, game):
        player = game.entities[0]
        p_x = player.s_x + player.width/2
        diff_y = player.s_y + player.width/2 - self.y_pos
        diff_x = player.s_x + player.width/2 - self.x_pos
        if self.velocity < 0:
            diff_xy = sqrt(diff_x**2 + diff_y**2)
            self.direction = -diff_x/(diff_xy)
            self.velocity = -diff_y/(diff_xy)

    #FIXME no ładne, polecam
    def move(self):
        self.y_pos -= self.velocity
        self.x_pos -= self.direction  # self.sidemove(self.player_start_x)

    #FIXME ekhem, no do gruntownego remontu to to
    def draw(self, GAME):  # TODO: tych argumentow jest troche duzo...
        if self.do_find_player_start_x and self.velocity < 0:
            self.find_player_start_x(GAME)
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
