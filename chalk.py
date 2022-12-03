from pico2d import *
import random

import server


class Chalk:
    MIN_FALL_SPEED = 5
    MAX_FALL_SPEED = 30
    heart_num = 3

    def __init__(self):
        self.x, self.y = random.randint(3000, 3500), 200
        self.chalk = load_image('resource/chalk.png')
        self.fall_speed = random.randint(Chalk.MIN_FALL_SPEED, Chalk.MAX_FALL_SPEED)

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.x -= self.fall_speed
        if self.x < 0:
            self.x = random.randint(3000, 4500)

    def draw(self):
        self.chalk.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, other, group):
        if group == 'character:chalk':
            server.character.score -= 20
            server.heart.heart_num -= 0.25

