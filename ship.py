class Ship:
    s_x = 0
    s_y = 0
    velocity = 0

    def __init__(self, given_x, given_y):
        self.s_x = given_x
        self.s_y = given_y

    def addVelocity(self, force):
        self.velocity += force
