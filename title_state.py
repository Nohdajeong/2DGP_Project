from pico2d import *
import game_framework

import main_state

background = None
logo = None
press = None

def enter():
    global background, logo, press
    background = load_image('Original.png')
    logo = load_image('logo.png')
    press = load_image('press_button.png')

def exit():
    global background, logo, press
    del background
    del logo
    del press

def update(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(main_state)

def draw():
    clear_canvas()
    background.draw(400, 310)
    press.draw(410, 250)
    logo.draw(410, 130)
    update_canvas()