from pygame import draw


class Bullet:
    velocity = 0
    x_pos = 0
    y_pos = 450
    exists = True

    def __init__(self, pos, force):
        self.x_pos = pos + 15
        self.velocity = force

    def move(self):
        self.y_pos -= self.velocity

    def draw(self, game_display, screen_y, entities, width, points):  # tych argumentow jest troche duzo...
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
            elif self.y_pos <= 0 or self.y_pos >= screen_y:
                self.exists = False
            if self.exists:
                draw.rect(game_display, (0, 0, 0), [self.x_pos, self.y_pos, 2, 10])
        return self.exists, points
