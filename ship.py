class Ship:
    s_x = 0
    s_y = 0
    velocity = 0
    width = 50
    height = 0
    is_enemy = False
    bullet_height = 50  # int(415/2)  # 20
    bullet_width = 5  # int(64/2)  # 4

    def __init__(self, given_x, given_y):
        self.s_x = given_x
        self.s_y = given_y

    def add_velocity(self, force):
        self.velocity += force

    def check_bullet(self, bullet):
        if bullet.velocity < 0 and self.is_enemy:
            return False
        if ((self.s_x < (bullet.x_pos + bullet.width)) and ((self.s_x + self.width) > bullet.x_pos)
                and (self.s_y < (bullet.y_pos + bullet.height)) and ((self.s_y + self.height) > bullet.y_pos)):
            return True
