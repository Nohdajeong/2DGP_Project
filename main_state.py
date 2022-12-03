from pico2d import *
import game_framework

import play_state

background = None
character = None
talk = None
time = 0.0

def enter():
    global background, character, talk
    background = load_image('School_main.png')
    character = load_image('run_character.png')
    talk = load_image('talk.png')

def exit():
    global background, character, talk
    del character
    del background
    del talk

def update():
    global time

    if (time > 0.7):
        time = 0
        game_framework.change_state(play_state)
    delay(0.01)
    time += 0.01

def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(play_state)

def draw():
    clear_canvas()
    background.draw(400, 220)
    character.draw(400, 300)
    talk.draw(250, 400)
    update_canvas()



