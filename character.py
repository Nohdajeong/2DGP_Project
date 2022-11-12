from pico2d import *

#1 : 이벤트 정의
UD, DD, UU, DU = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU
}


#2 : 상태 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir = 0

    @staticmethod
    def exit(self, event): pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 6

    @staticmethod
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 200, 200, self.x, self.y)


class JUMP:

    def enter(self, event):
        if event == UD:
            self.y += 100
        elif event == UU:
            self.y -= 100

    def exit(self, event): pass

    def do(self):
        self.frame = (self.frame + 1) % 6
        self.y += self.dir

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 200, 200, self.x, self.y)


class SLIDE:
    def enter(self, event):
        if event == DD:
            self.y -= 100
        elif event == DU:
            self.y += 100

    def exit(self, event): pass

    def do(self):
        self.frame = (self.frame + 1) % 6
        self.y -= self.dir

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 200, 200, self.x, self.y)



#3. 상태 변환 구현
next_state = {
    IDLE:   {UD: JUMP, UU: JUMP, DD: SLIDE, DU: SLIDE},
    JUMP:   {UD: JUMP, UU: JUMP, DD: SLIDE, DU: SLIDE},
    SLIDE:  {UD: JUMP, UU: JUMP, DD: SLIDE, DU: SLIDE}
}

class Character:
    def __init__(self):
        self.x, self.y = 0, 130
        self.frame = 0
        self.dir = 0
        self.image = load_image('run_animation_2.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


