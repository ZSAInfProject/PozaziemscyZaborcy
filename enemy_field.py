from math import ceil
from pygame import draw  # do usunięcia na koniec
import enemy_ship


class EnemyField:
    start_x = 50
    start_y = 50
    field_width = 100
    field_height = 200
    enemy_width = 0
    enemyHeight = 30
    velocity = 0.65
    offset_x = 0  # te offsety sa potrzebne globalnie w klasie, bo 2 funkcje z nich korzystaja a srednio mozna podac w argumentach
    offset_y = 0  # chyba ze ktos ma lepszy pomysl

    def __init__(self, screen_x, width):
        self.field_width = screen_x-100
        self.enemy_width = width

    def how_many_enemies(self):
        remainder_x = self.field_width % self.enemy_width
        remainder_y = self.field_height % self.enemyHeight
        how_many_x = int((self.field_width - remainder_x) / (self.enemy_width))
        how_many_y = int((self.field_height - remainder_y) / (self.enemyHeight))

        if how_many_x % 2 == 0:
            how_many_x /= 2
            remainder_x += self.enemy_width
        else:
            how_many_x = ceil(how_many_x / 2)
        if how_many_y % 2 == 0:
            how_many_y /= 2
            remainder_y += self.enemyHeight
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
            for _ in range(how_many_x):
                entities.append(enemy_ship.EnemyShip(self.enemy_width, field_offset_x, field_offset_y))
                field_offset_x += 2*self.enemy_width
            field_offset_y += 2*self.enemyHeight
        return entities

    def check_walls(self, screen_x, game_display):
        #draw.rect(game_display, (255, 0, 0), [self.start_x, self.start_y, self.field_width, self.field_height])
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

    def draw(self, screen_x, game_display, entities):
        if len(entities) > 1:  # update pola field'a
            min_x, max_x, min_y, max_y = self.find_entity_extremes(entities)
            self.start_x = min_x - self.offset_x
            self.field_width = round(max_x - self.start_x + entities[1].width) + self.offset_x
            self.start_y = min_y - self.offset_y
            self.field_height = round(max_y - self.start_y + entities[1].width) + self.offset_y
        if self.check_walls(screen_x, game_display):
            self.start_x += self.velocity
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 0)
        else:
            self.start_y += 20
            self.velocity *= -1
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 20)
