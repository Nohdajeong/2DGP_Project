from pico2d import *

class Character:
    def __init__(self):
        self.x, self.y = 0, 150
        self.frame = 0
        self.dir = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.y += self.dir * 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class IDLE:
    @staticmethod
    def enter():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


def handle_event(self, event):
    if event.type == SDL_KEYDOWN:
        match event.key:
            case pico2d.SDLK_UP:
                self.dir += 1
    elif event.type == SDL_KEYUP:
        match event.key:
            case pico2d.SDLK_UP:
                self.dir += 1
