import json
# import tomllib
import pickle
import os

from pico2d import *
import game_framework
import game_world

import play_state

from character import Character
from floor import Floor
from desk import Desk1

image = None

def enter():
    global image
    image = load_image('stop_select.png')
    hide_cursor()
    hide_lattice()

def exit():
    global image
    del image

def update(): pass

def draw():
    clear_canvas()
    play_state.draw_wolrd()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_F1:
                    game_framework.pop_state()
                case pico2d.SDLK_F2:
                    print('재시작')
                case pico2d.SDLK_F3:
                    print('도움말')

def pause(): pass

def resume(): pass


def test_self():
    import run_stop_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(run_stop_state)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()