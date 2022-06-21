from bullet import Bullet
from player_ship import PlayerShip


class BossBullet(Bullet):

    def __init__(self, pos_x, pos_y, force, half_entity_width, width, height, player, screen_y):
        super().__init__(pos_x, pos_y, force, half_entity_width, width, height)

        self.player: PlayerShip = player
        self.screen_y: int = screen_y
        self.die_timer: int = 0

    def update(self) -> None:
        # called every update so that it homes
        self.find_player_start_x(self.player)

        self.move()

        if self.player.check_bullet(self):
            self.player.damage()
            self.exists = False
        elif self.y_pos <= 0 or self.y_pos >= self.screen_y:
            self.exists = False

        # die after 400 ticks
        self.die_timer += 1
        if self.die_timer == 400:
            self.exists = False
