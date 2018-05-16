class Player:
    velocity = 0
    p_x = 250
    p_y = 450

    def move(self, speed):
        self.velocity += speed
        # testing
        print("velocity: ", self.velocity)

    def check_walls(self):
        if (round(self.p_x, 0) == 0 and self.velocity < 0) or (round(self.p_x, 0) == 470 and self.velocity > 0):
            return False
        else:
            return True
