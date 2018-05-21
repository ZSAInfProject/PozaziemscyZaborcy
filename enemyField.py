from math import ceil
from pygame import draw  # do usunięcia na koniec
import enemyShip


class EnemyField:
    startX = 50
    startY = 50
    fieldWidth = 100
    fieldHeight = 200
    enemyWidth = 0
    enemyHeight = 30
    velocity = 0.65
    offset_x = 0  # te offsety sa potrzebne globalnie w klasie, bo 2 funkcje z nich korzystaja a srednio mozna podac w argumentach
    offset_y = 0  # chyba ze ktos ma lepszy pomysl

    def __init__(self, screen_x, width):
        self.fieldWidth = screen_x-100
        self.enemyWidth = width

    def howManyEnemies(self):
        remainder_x = self.fieldWidth % self.enemyWidth
        remainder_y = self.fieldHeight % self.enemyHeight
        howMany_x = int((self.fieldWidth - remainder_x) / (self.enemyWidth))
        howMany_y = int((self.fieldHeight - remainder_y) / (self.enemyHeight))

        if howMany_x % 2 == 0:
            howMany_x /= 2
            remainder_x += self.enemyWidth
        else:
            howMany_x = ceil(howMany_x / 2)
        if howMany_y % 2 == 0:
            howMany_y /= 2
            remainder_y += self.enemyHeight
        else:
            howMany_y = ceil(howMany_y / 2)

        return howMany_x, remainder_x, howMany_y, remainder_y

    def fillWithEnemies(self, entities):
        howMany_x, remainder_x, howMany_y, remainder_y = self.howManyEnemies()
        self.offset_x = remainder_x/2
        self.offset_y = remainder_y/2
        fieldOffset_y = self.startY + self.offset_y
        for _ in range(int(howMany_y)):
            fieldOffset_x = self.startX + self.offset_x
            for _ in range(howMany_x):
                entities.append(enemyShip.EnemyShip(self.enemyWidth, fieldOffset_x, fieldOffset_y))
                fieldOffset_x += 2*self.enemyWidth
            fieldOffset_y += 2*self.enemyHeight
        return entities

    def checkWalls(self, screen_x, gameDisplay):
        draw.rect(gameDisplay, (255, 0, 0), [self.startX, self.startY, self.fieldWidth, self.fieldHeight])
        if (round(self.startX, 0) == 0 and self.velocity < 0) or (round(self.startX + self.fieldWidth, 0) == screen_x and self.velocity > 0):
            return False
        else:
            return True

    def findEntityExtremes(self, entities):
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

    def draw(self, screen_x, gameDisplay, entities):
        if len(entities) > 1:  # update pola field'a
            min_x, max_x, min_y, max_y = self.findEntityExtremes(entities)
            self.startX = min_x - self.offset_x
            self.fieldWidth = round(max_x - self.startX + entities[1].width) + 2 * self.offset_x
            self.startY = min_y - self.offset_y
            self.fieldHeight = round(max_y - self.startY + entities[1].width) + 2 * self.offset_y
        if self.checkWalls(screen_x, gameDisplay):
            self.startX += self.velocity
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 0)
        else:
            self.startY += 20
            self.velocity *= -1
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 20)
