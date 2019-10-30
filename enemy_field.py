from math import ceil
from random import uniform
from pygame import draw  # do usunięcia na koniec (TODO)
import enemy_ship


class EnemyField:
    start_x = 50
    start_y = 50
    field_width = 100
    field_height = 400
    enemy_width = enemy_ship.EnemyShip.width
    enemy_height = enemy_width
    velocity = 1.5  # 0.65
    offset_x = 0  # te offsety sa potrzebne globalnie w klasie, bo 2 funkcje z nich korzystaja a srednio mozna podac w argumentach
    offset_y = 0  # chyba ze ktos ma lepszy pomysl
    exists = True  # potrzebne tylko w rysowaniu ale nwm czy ma ktoś lepszy pomysł

    def __init__(self, screen_x, matej_model, bullet_model):
        self.field_width = screen_x/2  # -100
        self.model = matej_model
        self.bullet_model = bullet_model

    def how_many_enemies(self):
        remainder_x = self.field_width % self.enemy_width
        remainder_y = self.field_height % self.enemy_height
        how_many_x = int((self.field_width - remainder_x) / (self.enemy_width))
        how_many_y = int((self.field_height - remainder_y) /
                         (self.enemy_height))

        if how_many_x % 2 == 0:
            how_many_x /= 2
            remainder_x += self.enemy_width
        else:
            how_many_x = ceil(how_many_x / 2)
        if how_many_y % 2 == 0:
            how_many_y /= 2
            remainder_y += self.enemy_height
        else:
            how_many_y = ceil(how_many_y / 2)

        return how_many_x, remainder_x, how_many_y, remainder_y

    def fill_with_enemies(self, enemies):
        how_many_x, remainder_x, how_many_y, remainder_y = self.how_many_enemies()
        self.offset_x = remainder_x/2
        self.offset_y = remainder_y/2
        field_offset_y = self.start_y + self.offset_y
        for _ in range(int(how_many_y)):
            field_offset_x = self.start_x + self.offset_x
            for _ in range(int(how_many_x)):
                enemies.append(enemy_ship.EnemyShip(
                    field_offset_x, field_offset_y, self.enemy_width, self.model))
                field_offset_x += 2*self.enemy_width
            field_offset_y += 2*self.enemy_height
        return enemies

    def check_walls(self, screen_x):
        if (round(self.start_x, 0) <= 0 and self.velocity < 0) or (round(self.start_x + self.field_width, 0) >= screen_x and self.velocity > 0):
            return False
        else:
            return True

    def find_entity_extremes(self, enemies):
        min_x, min_y = float('Inf'), float('Inf')
        max_x, max_y = -float('Inf'), -float('Inf')

        for entity in range(0, len(enemies)):
            if enemies[entity].s_x < min_x:
                min_x = enemies[entity].s_x
            # musi byc if a nie elif, bo jesli zawsze bedzie true w 1szym, to nie ustawi max_x
            if enemies[entity].s_x > max_x:
                max_x = enemies[entity].s_x
            if enemies[entity].s_y < min_y:
                min_y = enemies[entity].s_y
            if enemies[entity].s_y > max_y:
                max_y = enemies[entity].s_y
        return min_x, max_x, min_y, max_y

    # self nie jest uzywany, wiec czy funkcja powinna byc tu gdzie jest?
    def find_shooter(self, enemies, player):
        min_distance = float('Inf')
        min_index = -1

        for entity in range(0, len(enemies)):
            current_distance = enemies[entity].distance_from_player(
                player.s_x, player.s_y, player.width)
            if current_distance <= min_distance:
                min_distance = current_distance
                min_index = entity
        return min_index

    def shot_calculation(self):
        pass

    def move_enemies(self, screen_x, enemies):
        if len(enemies) > 1:  # update pola field'a
            min_x, max_x, min_y, max_y = self.find_entity_extremes(enemies)
            self.start_x = min_x - self.offset_x
            self.field_width = round(
                max_x - self.start_x + enemies[1].width) + self.offset_x
            self.start_y = min_y - self.offset_y
            self.field_height = round(
                max_y - self.start_y + enemies[1].width) + self.offset_y
        else:
            self.exists = False
        if self.check_walls(screen_x):
            self.start_x += self.velocity
            for entity in range(0, len(enemies)):
                enemies[entity].move(self.velocity, 0)
        else:
            self.start_y += 65
            self.velocity *= -1
            for entity in range(0, len(enemies)):
                enemies[entity].move(self.velocity, 65)
