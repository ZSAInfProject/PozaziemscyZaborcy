class Bullet:
    velocity = 0
    x = 0
    y = 450

    def __init__(self, pos):
        self.x = pos + 15
        self.velocity = 2

    def move(self):
        self.y -= self.velocity
