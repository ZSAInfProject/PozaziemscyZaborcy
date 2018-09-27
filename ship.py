#FIXME skalowanie daje mi raka
class Ship:
    s_x = 0
    s_y = 0
    velocity = 0
    width = 50
    height = 0
    is_enemy = False
    bullet_height = int(415/2)  # 20
    bullet_width = int(64/2)  # 4

    #FIXME git
    def __init__(self, given_x, given_y):
        self.s_x = given_x
        self.s_y = given_y

    #FIXME spoko
    def add_velocity(self, force):
        self.velocity += force

    #FIXME elif na dwa monitory
    def check_bullet(self, bullet):
        if bullet.velocity < 0 and self.is_enemy:
            return False
        elif (self.s_y <= bullet.y_pos + bullet.height <= self.s_y + self.height) and (self.s_x <= bullet.x_pos + bullet.width <= self.s_x + self.width):
            return True
