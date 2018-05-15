class Bullet:
    speed = 0
    x = 0
    y = 450

    def __init__(self, pos):
        self.x = pos
        self.speed = 0.1

    def move(self):
        self.y -= self.speed