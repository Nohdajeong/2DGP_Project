from pico2d import *

import server

class BackGround:
    def __init__(self):
        self.image = load_image('School_stage1.png')

    def draw(self):
        self.image.draw(400, 220)
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)

    def update(self):
        # quadrant 3
        self.q3l = (int(server.character.x) - self.canvas_width // 2) % self.w
        self.q3b = (int(server.character.y) - self.canvas_height // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.canvas_height - self.q3w

        # quadrand 4
        self.q4l = 0
        self.q4b = 0
        self.q4w = 0
        self.q4h = 0

        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = 0
        self.q1h = 0

    def handle_event(self, event):
        pass
