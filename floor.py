from pico2d import *

class Floor:
    def __init__(self):
        self.floor = load_image('floor.png')

    def draw(self):
        self.floor.draw(400, 30)

    def update(self): pass

    def get_bb(self):
        return 0, 0, 1600-1, 50