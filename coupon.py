from pico2d import *
import game_framework
import game_world
import random

class Coupon:
    image = None

    def __init__(self):
        if Coupon.image == None:
            Coupon.image = load_image('Gold Ticket.png')
        self.x, self.y = random.randint(0, get_canvas_width()-1), 220


    def __getstate__(self):
        state = {'x':self.x, 'y':self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def handle_collision(self, other, grou):
        game_world.remove_object(self)