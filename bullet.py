from pygame import draw


class Bullet:
    velocity = 0
    x = 0
    y = 450
    exists = True

    def __init__(self, pos, force):
        self.x = pos + 15
        self.velocity = force

    def move(self):
        self.y -= self.velocity

    def draw(self, gameDisplay, screen_y, entities, width, points):  # tych argumentow jest troche duzo...
        self.move()
        for i, entity in enumerate(entities):  # bez range sie krzaczy przy usuwaniu entity (24 linia)
            # tutaj zmienia sie poziom trudnosci
            if entity.check_bullet(self, width):  # powinnismy rozrozniac width gracza i wroga, chyba?
                self.exists = False
                if self.velocity > 0:
                    del entities[i]
                    points += 10
                    break
                elif self.velocity < 0:
                    points -= 10
                    print('game over')
                else:
                    print('this should never appear')
            elif self.y <= 0 or self.y >= screen_y:
                self.exists = False
            if self.exists:
                draw.rect(gameDisplay, (0, 0, 0), [self.x, self.y, 2, 10])
        return self.exists, points
