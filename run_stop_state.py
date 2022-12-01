import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import server

import play_state

from character import Character
from background import BackGround
from floor import Floor
from desk import Desk1
from heart import Heart
from coupon import Coupon

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

def pause(): pass

def resume(): pass

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
                    create_new_world()
                    game_framework.change_state(play_state)
                case pico2d.SDLK_F2:
                    load_saved_world()
                    game_framework.change_state(play_state)
                case pico2d.SDLK_F3:
                    print('도움말')

def create_new_world():
    server.character = Character()
    game_world.add_object(server.character, 1)
    game_world.add_collision_pairs(server.character, None, 'Character:desk')
    game_world.add_collision_pairs(server.character, None, 'Character:coupon')

    background = BackGround()
    game_world.add_object(background, 0)

    coupons = [Coupon for i in range(50)]
    game_world.add_objects(coupons, 1)
    game_world.add_collision_pairs(None, coupons, 'Character:Coupon')

def load_saved_world():
    game_world.load()
    for o in game_world.add_objects():
        if isinstance(o, Character):
            server.character = o
            break

def test_self():
    import run_stop_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(run_stop_state)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()