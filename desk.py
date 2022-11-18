from pico2d import *
import random

class Desk1:
    def __init__(self):
        self.dx1, self.dy1 = random.randint(800, 1500), 100
        self.desk1 = load_image('desk_1.png')

    def update(self):
        self.dx1 -= 20
        if self.dx1 < 0:
            self.dx1 = random.randint(800, 1500)

    def draw(self):
        self.desk1.draw(self.dx1, self.dy1)

    def get_bb(self):
        return self.dx1 - 10, self.dy1 - 10, self.dx1 + 10, self.dy1 + 10

class Desk2:
    def __init__(self):
        self.dx2, self.dy2 = random.randint(800, 1500), 170
        self.desk2 = load_image('desk_2.png')

    def update(self):
        self.dx2 -= 20
        if self.dx2 < 0:
            self.dx2 = random.randint(800, 1500)

    def draw(self):
        self.desk2.draw(self.dx2, self.dy2)

    def get_bb(self):
        return self.dx2 - 10, self.dy2 - 10, self.dx2 + 10, self.dy2 + 10

