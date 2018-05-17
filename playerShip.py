import ship


class PlayerShip(ship.Ship):

    def __init__(self, given_x=220, given_y=450):
        self.s_x = given_x
        self.s_y = given_y

    def check_walls(self):
        if (round(self.s_x, 0) == 0 and self.velocity < 0) or (round(self.s_x, 0) == 470 and self.velocity > 0):
            return False
        else:
            return True
