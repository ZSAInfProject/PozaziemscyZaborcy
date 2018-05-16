import ship


class PlayerShip(ship.Ship):
    def __init__(self, p_x=250, p_y=450):
        self.p_x = p_x
        self.p_y = p_y

    def check_walls(self):
        if (round(self.p_x, 0) == 0 and self.velocity < 0) or (round(self.p_x, 0) == 470 and self.velocity > 0):
            return False
        else:
            return True
