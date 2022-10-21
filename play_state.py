import game_framework
from pico2d import *
import random

import run_stop_state

class BackGround:
    def __init__(self):
        self.image = load_image('School_stage1.png')

    def draw(self):
        self.image.draw(400, 220)


class Floor:
    def __init__(self):
        self.floor = load_image('floor.png')

    def draw(self):
        self.floor.draw(400, 30)

class Desk:
    def __init__(self):
        self.dx1, self.dy1 = random.randint(800, 1500), 100
        self.dx2, self.dy2 = random.randint(800, 1500), 170
        self.desk1 = load_image('desk_1.png')
        self.desk2 = load_image('desk_2.png')

    def update(self):
        self.dx1 -= 1
        self.dx2 -= 1
        if self.dx1 < 0:
            self.dx1 = random.randint(800, 1500)
        if self.dx2 < 0:
            self.dx2 = random.randint(800, 1500)

    def draw(self):
        self.desk1.draw(self.dx1, self.dy1)
        self.desk2.draw(self.dx2, self.dy2)


class Floor:
    def __init__(self):
        self.floor = load_image('floor.png')

    def draw(self):
        self.floor.draw(400, 30)

# class Ruler:
#    def __init__(self):
#        self.rx, self.ry = 600, 100
#        self.ruler = load_image('ruler.png')

#    def update(self):
#        self.rx += 1

#   def draw(self):
#        self.ruler.draw(self.rx, self.ry)

class Character:
    def __init__(self):
        self.x, self.y = 0, 150
        self.frame = 0
        self.image = load_image('run.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(self.frame*220, 0, 400, 250, self.x, self.y)



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


floor = None
desk = None
background = None
character = None
running = True

# 초기화
def enter():
    global background, floor, desk, character, running
    background = BackGround()
    floor = Floor()
    desk = Desk()
    character = Character()
    running = True

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

