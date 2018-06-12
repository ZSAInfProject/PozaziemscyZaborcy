class Ship:
    s_x = 0
    s_y = 0
    velocity = 0
    width = 50
    height = 0
    is_enemy = False
    bullet_height = 20
    bullet_width = 4

    def __init__(self, given_x, given_y):
        self.s_x = given_x
        self.s_y = given_y

    def add_velocity(self, force):
        self.velocity += force

    def check_bullet(self, bullet):
        if bullet.velocity < 0 and self.is_enemy:
            return False
        elif (self.s_y <= bullet.y_pos + bullet.height <= self.s_y + self.height) and (self.s_x <= bullet.x_pos + bullet.width <= self.s_x + self.width):
            return True
