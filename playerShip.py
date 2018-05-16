import ship


class PlayerShip(ship.Ship):
    def __init__(self, given_x=250, given_y=450):
        self.p_x = given_x
        self.p_y = given_y

    def check_walls(self):
        if (round(self.p_x, 0) == 0 and self.velocity < 0) or (round(self.p_x, 0) == 470 and self.velocity > 0):
            return False
        else:
            return True
