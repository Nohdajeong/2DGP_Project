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
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 6

    @staticmethod
    def draw(self):
        pass


class JUMP:
    def enter(self, event):
        print('ENTER JUMP')
        if event == UD:
            self.y += 20
        elif event == UU:
            self.y -= 20

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        pass


class SLIDE:
    def enter(self, event):
        print('ENTER SLIDE')
        if event == DD:
            self.y -= 20
        elif event == DU:
            self.y += 20

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        pass


#3. 상태 변환 구현
next_state = {
    IDLE:   {UD: JUMP, UU:IDLE, DD: SLIDE, DU: IDLE},
    JUMP:   {UD: JUMP, UU:IDLE, DD: SLIDE, DU: IDLE},
    SLIDE:  {UD: JUMP, UU:IDLE, DD: SLIDE, DU: IDLE}
}

class Character:
    def __init__(self):
        self.x, self.y = 0, 150
        self.frame = 0
        self.dir = 0
        self.image = load_image('run_animation.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter()

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.y += self.dir * 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_event(self, event):
    if event.type == SDL_KEYDOWN:
        match event.key:
            case pico2d.SDLK_UP:
                self.dir += 1
    elif event.type == SDL_KEYUP:
        match event.key:
            case pico2d.SDLK_UP:
                self.dir += 1
