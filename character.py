import game_framework
from pico2d import *

import game_world
import server

# Action Speed
TIME_PER_ACTION = 0.05
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION


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
    def enter(character, event):
        character.x, character.y = 100, 130
        character.dir = 0

    @staticmethod
    def exit(character, event): pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + 1) % 4

    @staticmethod
    def draw(character):
        character.run.clip_draw(int(character.frame)*200, 0, 200, 200, character.x, character.y)
        delay(0.05)


class JUMP:

    def enter(character, event):
        if event == UD:
            character.y += 120
        elif event == UU:
            character.y -= 120

    def exit(character, event): pass

    def do(character):
        character.frame = (character.frame + 1) % 3

    def draw(character):
        character.jump.clip_draw(int(character.frame)*200, 0, 200, 200, character.x, character.y)
        delay(0.05)


class SLIDE:
    def enter(character, event):
        character.x,character.y = 100, 80

    def exit(character, event): pass

    def do(character):
        character.frame = (character.frame + 1) % 2

    def draw(character):
        character.slide.clip_draw(int(character.frame)*200, 0, 200, 100, character.x, character.y)
        delay(0.05)



#3. 상태 변환 구현
next_state = {
    IDLE:   {UD: JUMP, UU: JUMP, DD: SLIDE, DU: SLIDE},
    JUMP:   {UD: JUMP, UU: IDLE, DD: SLIDE, DU: IDLE},
    SLIDE:  {UD: JUMP, UU: JUMP, DD: SLIDE, DU: IDLE}
}

class Character:
    def __init__(self):
        self.x, self.y = 100, 130
        self.frame = 0
        self.run = load_image('run_animation.png')
        self.jump = load_image('jump.png')
        self.slide = load_image('slide.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50
