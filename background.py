from pico2d import *

import server

class BackGround:
    def __init__(self):
        self.image = load_image('School_stage1.png')

    def draw(self):
        self.image.draw(400, 220)

    def update(self):
        pass

    def handle_event(self, event):
        pass
