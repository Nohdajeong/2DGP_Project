from pico2d import *

#1 : 이벤트 정의
UD, DD, UU, DU = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP) : UD,
    (SDL_KEYDOWN, SDLK_DOWN) : DD,
    (SDL_KEYUP, SDLK_UP) : UU,
    (SDL_KEYUP, SDLK_DOWN) : DU
}


#2 : 상태 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0

    @staticmethod
    def exit(self):
        print('EXIT IDLE')


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
