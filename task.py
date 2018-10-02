from random import uniform


class Task:
    def __init__(self, name, interval, offset, tickrate):
        self.name = name
        self.base_interval = interval
        self.offset_min = offset[0]
        self.offset_max = offset[1]
        self.offset = self.generate_offset()
        self.ticks_remaining = self.update_interval(self.randomize_operator()) * tickrate

    def generate_offset(self):
        return uniform(self.offset_min, self.offset_max)

    def update_interval(self, add):
        if add:
            self.interval = self.base_interval + self.generate_offset()
        else:
            self.interval = self.base_interval - self.generate_offset()
        return self.interval

    def randomize_operator(self):
        return round(uniform(0, 1))

    def check_ticks(self, tickrate):
        self.ticks_remaining -= 1
        if self.ticks_remaining <= 0:
            self.ticks_remaining = self.update_interval(self.randomize_operator()) * tickrate
            return True
        return False
