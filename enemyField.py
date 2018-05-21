from pygame import draw #do usunięcia na koniec
from math import ceil
import enemyShip


class EnemyField:
    startX = 50
    startY = 50
    fieldWidth = 100
    fieldHeight = 200
    enemyWidth = 0
    enemyHeight = 30
    velocity = 0.65

    def __init__(self, screen_x, width):
        self.fieldWidth = screen_x-100
        self.enemyWidth = width


    def howManyEnemies(self):
        remainder_x = self.fieldWidth % self.enemyWidth
        remainder_y = self.fieldHeight % self.enemyHeight
        howMany_x = ceil((self.fieldWidth - remainder_x) / (self.enemyWidth * 2))
        howMany_y = ceil((self.fieldHeight - remainder_y) / (self.enemyHeight * 2))
        return howMany_x, remainder_x, howMany_y, remainder_y

    def fillWithEnemies(self, entities):
        howMany_x, remainder_x, howMany_y, remainder_y = self.howManyEnemies()
        offset_x = remainder_x/2
        offset_y = remainder_y/2
        fieldOffset = self.startX + offset_x
        for adversary in range(howMany_x):
            entities.append(enemyShip.EnemyShip(self.enemyWidth, fieldOffset, self.startY))
            fieldOffset += 2*self.enemyWidth
        return entities

    def checkWalls(self, screen_x, gameDisplay):
        #draw.rect(gameDisplay, (255, 0, 0), [self.startX, self.startY, self.fieldWidth, self.fieldHeight])
        if (round(self.startX, 0) == 0 and self.velocity < 0) or (round(self.startX + self.fieldWidth, 0) == screen_x and self.velocity > 0):
            return False
        else:
            return True

    def draw(self, screen_x, gameDisplay, entities):
        if self.checkWalls(screen_x, gameDisplay):
            self.startX += self.velocity
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 0)
        else:
            self.startY += 20
            self.velocity *= -1
            for entity in range(1, len(entities)):
                entities[entity].move(self.velocity, 20)
