from pico2d import *
import game_world

class Heart:
    heart = None

    def __init__(self):
        self.x, self.y = 670, 550
        self.heart = load_image('resource/heart.png')
        self.heart_num = 5

    def update(self):
        pass

    def draw(self):
        self.heart.draw(self.x, self.y)