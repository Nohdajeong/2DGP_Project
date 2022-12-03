from pico2d import *
import random

import server


class Desk1:
    MIN_FALL_SPEED = 5
    MAX_FALL_SPEED = 30
    heart_num = 3

    def __init__(self):
        self.dx1, self.dy1 = random.randint(1000, 1500), 100
        self.desk1 = load_image('resource/desk_1.png')
        self.fall_speed = random.randint(Desk1.MIN_FALL_SPEED, Desk1.MAX_FALL_SPEED)

    def __getstate__(self):
        state = {'x': self.dx1, 'y': self.dy1}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.dx1 -= self.fall_speed
        if self.dx1 < 0:
            self.dx1 = random.randint(1000, 1500)

    def draw(self):
        self.desk1.draw(self.dx1, self.dy1)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.dx1 - 30, self.dy1 - 30, self.dx1 + 30, self.dy1 + 30

    def handle_collision(self, other, group):
        if group == 'character:desk':
            server.character.score -= 20
            server.heart.heart_num -= 0.25

        if group == 'desk:coupon':
            pass

        if group == 'desk:desk':
            self.desk1.draw(self.dx1 - 100, self.dy1)
