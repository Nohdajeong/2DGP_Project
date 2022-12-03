from pico2d import *
import game_framework

import play_state
import main_state

background = None
logo = None
press = None
bgm = None

def enter():
    global background, logo, press, bgm
    background = load_image('resource/Original.png')
    logo = load_image('resource/logo.png')
    press = load_image('resource/press_button.png')
    bgm = load_music('resource/bgm_lobby.ogg')
    bgm.set_volume(32)
    bgm.repeat_play()

def exit():
    global background, logo, press, bgm
    del background
    del logo
    del press
    del bgm

def update(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            # game_framework.change_state(play_state)
            game_framework.change_state(main_state)


def draw():
    clear_canvas()
    background.draw(400, 310)
    press.draw(410, 250)
    logo.draw(410, 130)
    update_canvas()