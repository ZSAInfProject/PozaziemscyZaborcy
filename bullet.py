from pygame import draw


class Bullet:
    velocity = 0
    x_pos = 0
    y_pos = 0
    exists = True

    def __init__(self, pos_x, pos_y, force):
        self.x_pos = pos_x + 15  # TODO: zamiast tego 15 powinna byc polowa width strzelajacego entity
        self.y_pos = pos_y
        self.velocity = force

    def move(self):
        self.y_pos -= self.velocity

    def draw(self, GAME):  # TODO: tych argumentow jest troche duzo...
        self.move()
        for i, entity in enumerate(GAME.entities):  # bez range sie krzaczy przy usuwaniu entity (24 linia)
            # tutaj zmienia sie poziom trudnosci
            if entity.check_bullet(self, GAME.width):  # TODO: powinnismy rozrozniac width gracza i wroga, chyba?
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
            if self.exists:
                draw.rect(GAME.game_display, (0, 0, 0), [self.x_pos, self.y_pos, 2, 10])
        return self.exists, GAME.points
