from pico2d import *
import game_framework
import game_world
import random

# coupon speed
PIXER_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXER_PER_METER)

class Coupon:
    def __init__(self):
        self.x, self.y = 800, 100
        self.image = load_image('Gold Ticket.png')

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        # for i in range(10):
        #     self.image.draw(self.x, self.y)
        # draw_rectangle(*self.get_bb())
        pass

    def do(self):
        self.x += self.x * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600-25)

    def update(self):
        self.x -= 20
        if self.x < 0:
            self.x = self.x-20

    def handle_collision(self, other, group):
        if group == 'character:coupon':
            game_world.remove_object(self)