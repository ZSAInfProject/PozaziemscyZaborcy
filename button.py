from pygame import draw


class Button:
    def __init__(self, x_0, y_0, width, height, colour, outline=0):  # TODO: dodac offset I guess
        self.x_0 = x_0
        self.y_0 = y_0
        self.width = width
        self.height = height
        self.colour = colour
        self.outline = outline

    def draw(self, game_display):
        draw.rect(game_display, self.colour, (self.x_0, self.y_0, self.width, self.height), self.outline)
