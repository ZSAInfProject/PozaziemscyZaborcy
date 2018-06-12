from math import ceil
from random import uniform
from pygame import draw  # do usunięcia na koniec
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
        how_many_y = int((self.field_height - remainder_y) / (self.enemy_height))

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

    def fill_with_enemies(self, entities):
        how_many_x, remainder_x, how_many_y, remainder_y = self.how_many_enemies()
        self.offset_x = remainder_x/2
        self.offset_y = remainder_y/2
        field_offset_y = self.start_y + self.offset_y
        for _ in range(int(how_many_y)):
            field_offset_x = self.start_x + self.offset_x
            for _ in range(int(how_many_x)):
                entities.append(enemy_ship.EnemyShip(field_offset_x, field_offset_y, self.enemy_width, self.model, self.bullet_model))
                field_offset_x += 2*self.enemy_width
            field_offset_y += 2*self.enemy_height
        return entities

    def check_walls(self, screen_x, game_display):
        # print(screen_x)
        if (round(self.start_x, 0) <= 0 and self.velocity < 0) or (round(self.start_x + self.field_width, 0) >= screen_x and self.velocity > 0):
            return False
        else:
            return True

    def find_entity_extremes(self, entities):
        min_x, min_y = float('Inf'), float('Inf')
        max_x, max_y = -float('Inf'), -float('Inf')

        for entity in range(1, len(entities)):
            if entities[entity].s_x < min_x:
                min_x = entities[entity].s_x
            if entities[entity].s_x > max_x:  # musi byc if a nie elif, bo jesli zawsze bedzie true w 1szym, to nie ustawi max_x
                max_x = entities[entity].s_x
            if entities[entity].s_y < min_y:
                min_y = entities[entity].s_y
            if entities[entity].s_y > max_y:
                max_y = entities[entity].s_y
        return min_x, max_x, min_y, max_y

    def find_shooter(self, entities):  # self nie jest uzywany, wiec czy funkcja powinna byc tu gdzie jest?
        min_distance = float('Inf')
        min_index = -1

        for entity in range(1, len(entities)):
            current_distance = entities[entity].distance_from_player(entities[0].s_x, entities[0].s_y, entities[0].width)
            if current_distance <= min_distance:
                min_distance = current_distance
                min_index = entity
        return min_index

    def shot_calculation(self):
        pass

    def draw(self, screen_x, game_display, entities):
        if len(entities) > 1:  # update pola field'a
            #draw.rect(game_display, (255, 0, 0), (self.start_x, self.start_y, self.field_width, self.field_height))
            min_x, max_x, min_y, max_y = self.find_entity_extremes(entities)
            self.start_x = min_x - self.offset_x
            self.field_width = round(max_x - self.start_x + entities[1].width) + self.offset_x
            self.start_y = min_y - self.offset_y
            self.field_height = round(max_y - self.start_y + entities[1].width) + self.offset_y
        else:
            self.exists = False
        if self.check_walls(screen_x, game_display):
            self.start_x += self.velocity
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 0)
        else:
            self.start_y += 65
            self.velocity *= -1
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 65)
