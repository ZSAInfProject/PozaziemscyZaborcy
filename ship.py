class Ship:
    s_x = 0
    s_y = 0
    velocity = 0
    width = 50
    height = 0
    is_enemy = False
    bullet_height = int(415/2)  # 20
    bullet_width = int(64/2)  # 4

    def __init__(self, given_x, given_y):
        self.s_x = given_x
        self.s_y = given_y

    def add_velocity(self, force):
        self.velocity += force

    def check_bullet(self, bullet):
        if bullet.velocity < 0 and self.is_enemy:
            return False
        temp_y = self.s_y
        temp_x = self.s_x
        if self.is_enemy:
            #temp_y += self.height
            pass
        if (temp_y <= bullet.y_pos + bullet.height <= temp_y + self.height) and (temp_x <= bullet.x_pos + bullet.width <= temp_x + self.width):
            return True
