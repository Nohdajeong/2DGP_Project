import game_framework
from pico2d import *

import play_state

running = True
background = None
character = None

def enter():
    global background, character
    background = load_image('School_main.png')
    character = load_image('run_character.png')
    pass

def exit():
    global background, character
    del character
    del background
    pass

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(play_state)
    delay(0.01)


def draw():
    clear_canvas()
    background.draw(400, 220)
    character.draw(400, 300)
    update_canvas()



