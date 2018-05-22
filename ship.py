class Ship:
    s_x = 0
    s_y = 0
    velocity = 0
    width = 0

    def __init__(self, given_x, given_y):
        self.s_x = given_x
        self.s_y = given_y

    def add_velocity(self, force):
        self.velocity += force

    def check_bullet(self, bullet, width):
        if (self.s_y <= bullet.y_pos <= self.s_y + width) and (self.s_x <= bullet.x_pos <= self.s_x + width):
            return True
