from pico2d import *
import server
import random

class Ruler:
    MIN_FALL_SPEED = 5
    MAX_FALL_SPEED = 30
    def __init__(self):
        self.rx, self.ry = 800, 600
        self.ruler = load_image('ruler.png')
        self.fall_speed = random.randint(Ruler.MIN_FALL_SPEED, Ruler.MAX_FALL_SPEED)

    def __getstate__(self):
        state = {'x': self.rx, 'y': self.ry}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.rx -= self.fall_speed
        if self.rx < 0:
            self.rx = random.randint(800, 1500)


    def draw(self):
        self.ruler.draw(self.rx, self.ry)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.rx - 50, self.ry - 100, self.rx + 50, self.ry + 100

    def handle_collision(self, other, group):
        if group == 'character:ruler':
            server.character.score -= 20
            server.heart.heart_num -= 0.25
