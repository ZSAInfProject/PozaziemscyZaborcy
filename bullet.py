from pygame import transform
from math import sqrt
from resources import Resources


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
        self.bullet_model = transform.scale(
            Resources.bullet_model, (self.width, self.height))

        self.original_velocity = force

    def find_player_start_x(self, player):
        player = player
        diff_y = player.s_y - self.y_pos - self.height/2
        diff_x = player.s_x + player.width/2 - self.x_pos
        if self.velocity < 0:
            diff_xy = sqrt(diff_x**2 + diff_y**2)
            self.direction = -diff_x / diff_xy
            self.velocity = max(-diff_y / diff_xy, self.original_velocity)

    def move(self):
        self.y_pos -= self.velocity
        self.x_pos -= self.direction  # self.sidemove(self.player_start_x)

    def draw(self, GAME):  # TODO: tych argumentow jest troche duzo...
        if self.do_find_player_start_x and self.velocity < 0:
            self.find_player_start_x(GAME.player)
            self.do_find_player_start_x = False
        self.move()
        # bez range sie krzaczy przy usuwaniu entity (24 linia)
        for i, entity in enumerate(GAME.enemies):
            # tutaj zmienia sie poziom trudnosci
            # TODO: powinnismy rozrozniac width gracza i wroga, chyba?
            if entity.check_bullet(self):
                self.exists = False
                if self.velocity > 0:
                    del GAME.enemies[i]
                    GAME.points += 10
                    break
                elif self.y_pos <= 0 or self.y_pos >= GAME.screen_y:
                    self.exists = False
                else:
                    print('this should never appear')
        if GAME.player.check_bullet(self):
            if self.velocity < 0:
                GAME.points -= 10
                GAME.game_end = True
                GAME.game_lost = True
        return self.exists, GAME.points
