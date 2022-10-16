import game_framework
from pico2d import *
import random

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


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


floor = None
desk = None
background = None
running = True

# 초기화
def enter():
    global background, floor, desk, running
    background = BackGround()
    floor = Floor()
    desk = Desk()
    running = True

def exit():
    global background, floor, desk
    del background
    del floor
    del desk


def update():
    desk.update()


def draw():
    clear_canvas()
    background.draw()
    floor.draw()
    desk.draw()
    update_canvas()

