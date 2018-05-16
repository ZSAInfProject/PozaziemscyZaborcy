class Ship:
    p_x = 0
    p_y = 0
    velocity = 0

    def __init__(self, p_x, p_y):
        self.p_x = p_x
        self.p_y = p_y

    def addVelocity(self, velocity):
        self.velocity += velocity
