class Ship:
    p_x = 0
    p_y = 0
    velocity = 0

    def __init__(self, given_x, given_y):
        self.p_x = given_x
        self.p_y = given_y

    def addVelocity(self, force):
        self.velocity += force
