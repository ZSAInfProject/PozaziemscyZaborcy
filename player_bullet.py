from bullet import Bullet


class PlayerBullet(Bullet):

    def __init__(self, pos_x, pos_y, force, half_entity_width, width, height, boss, screen_y):
        super().__init__(pos_x, pos_y, force, half_entity_width, width, height)

        self.boss = boss
        self.screen_y = screen_y

    def update(self) -> None:
        self.move()

        if self.boss.check_bullet(self):
            self.boss.damage()
            self.exists = False
        elif self.y_pos <= 0 or self.y_pos >= self.screen_y:
            self.exists = False
