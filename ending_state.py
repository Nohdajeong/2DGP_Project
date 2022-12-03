from pico2d import *
import game_framework

endimage = None

def enter():
    global endimage
    endimage = load_image('end.png')

def exit():
    global endimage
    del endimage

def update(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def draw():
    clear_canvas()
    endimage.draw(400, 310)
    update_canvas()