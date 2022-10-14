from pico2d import *
import game_framework

class BackGround:
    def __init__(self):
        self.image = load_image('School_stage1.png')

    def draw(self):
        self.image.draw(400, 220)


class Object:
    def __init__(self):
        self.floor = load_image('floor.png')
        self.desk1 = load_image('desk_1.png')
        self.desk2 = load_image('desk_2.png')

    def draw(self):
        self.floor.draw(400, 30)
        self.desk1.draw(420, 100)
        self.desk2.draw(200, 170)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

object = None
background = None
running = True

# 초기화
def enter():
    global background, object, running
    background = BackGround()
    object = Object()
    running = True

def exit():
    global background, object
    del background
    del object

def update():
    pass

def draw():
    clear_canvas()
    background.draw()
    object.draw()
    update_canvas()

