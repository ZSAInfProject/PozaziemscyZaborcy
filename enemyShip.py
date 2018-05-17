import ship


class EnemyShip(ship.Ship):

    def __init__(self, given_x=220, given_y=50):
        self.s_x = given_x
        self.s_y = given_y
        self.velocity = 1

    def check_walls(self):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == 470 and self.velocity > 0):
            return False
        else:
            return True

    def check_bullet(self, bull):
        if bull.y == self.s_y + 30 and (self.s_x <= bull.x <= self.s_x + 30):
            return True

    def check_player(self, player):
        print('ok')
        if (self.s_y + 30 >= player.s_y >= self.s_y) and (self.s_x + 30 >= player.s_x >= self.s_x):
            print('not ok')
            return True