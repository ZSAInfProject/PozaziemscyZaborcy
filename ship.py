class Ship:
    s_x = 0
    s_y = 0
    velocity = 0
    width = 50
    height = 0
    is_enemy = False
    bullet_height = 50
    bullet_width = 5

    def __init__(self, given_x, given_y):
        self.s_x: float = given_x
        self.s_y: float = given_y

    def add_velocity(self, force):
        self.velocity += force

    def check_bullet(self, bullet):
        if bullet.velocity < 0 and self.is_enemy:
            return False
        if ((self.s_x < (bullet.x_pos + bullet.width)) and ((self.s_x + self.width) > bullet.x_pos)
                and (self.s_y < (bullet.y_pos + bullet.height)) and ((self.s_y + self.height) > bullet.y_pos)):
            return True
