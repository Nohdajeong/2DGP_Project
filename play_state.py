import pico2d

import game_framework
from pico2d import *

import run_stop_state

from character import Character
from floor import Floor
from background import BackGround
from desk import Desk


# class Ruler:
#    def __init__(self):
#        self.rx, self.ry = 600, 100
#        self.ruler = load_image('ruler.png')

#    def update(self):
#        self.rx += 1

#   def draw(self):
#        self.ruler.draw(self.rx, self.ry)

floor = None
desk = None
background = None
character = None

running = True


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_i:
                    game_framework.push_state(run_stop_state)
                case pico2d.SDLK_1:
                    # 스킬 수행 - 1
                    pass
                case pico2d.SDLK_2:
                    pass
        else:
            character.handle_event(event)


# 초기화
def enter():
    global background, floor, desk, character, running
    background = BackGround()
    floor = Floor()
    desk = Desk()
    character = Character()
    running = True

# 종료
def exit():
    global background, floor, desk, character
    del background
    del floor
    del desk
    del character


def update():
    desk.update()
    character.update()

def draw():
    clear_canvas()
    draw_wolrd()
    update_canvas()

def draw_wolrd():
    background.draw()
    floor.draw()
    desk.draw()
    character.draw()

def pause():
    pass

def resume():
    pass

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

