from pico2d import *

class Heart:
    heart1 = None
    heart2 = None
    heart3 = None

    def __init__(self):
        self.x1, self.y1 = 730, 550
        self.x2, self.y2 = 670, 550
        self.x3, self.y3 = 610, 550
        self.heart1 = load_image('heart.png')
        self.heart2 = load_image('heart.png')
        self.heart3 = load_image('heart.png')

    def update(self):
        pass

    def draw(self):
        self.heart1.draw(self.x1, self.y1)
        self.heart2.draw(self.x2, self.y2)
        self.heart3.draw(self.x3, self.y3)