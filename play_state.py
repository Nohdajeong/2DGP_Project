from pico2d import *
import game_framework
import game_world
import server

import json
import pickle
import os

import run_stop_state
import ending_state

from character import Character
from floor import Floor
from background import BackGround
from desk import Desk1
from heart import *
from coupon import Coupon
from ruler import Ruler

score = 0
heart_num = 3
skill_num = 1

time = None
font = None
running = True


def handle_events():
    global skill_num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(run_stop_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            if skill_num == 1:
                skill_num -= 1
                server.heart.heart_num += 1
        else:
            server.character.handle_event(event)


# 초기화
def enter():
    # back
    background = BackGround()
    floor = Floor()
    game_world.add_object(background, 0)
    game_world.add_object(floor, 0)

    # object
    server.desks = [Desk1() for i in range(2)]
    game_world.add_objects(server.desks, 1)
    game_world.add_collision_pairs(None, server.desks, 'character:desk')
    # game_world.add_collision_pairs(None, server.desks, 'desk:coupon')
    game_world.add_collision_pairs(None, server.desks, 'desk:ruler')
    game_world.add_collision_pairs(server.desks, server.desks, 'desk:desk')

    server.ruler = Ruler()
    game_world.add_object(server.ruler, 1)
    game_world.add_collision_pairs(None, server.ruler, 'character:ruler')
    game_world.add_collision_pairs(None, server.ruler, 'desk:ruler')


    # character
    server.character = Character()
    game_world.add_object(server.character, 2)
    game_world.add_collision_pairs(server.character, None, 'character:desk')
    # game_world.add_collision_pairs(server.character, None, 'character:coupon')
    game_world.add_collision_pairs(server.character, None, 'character:ruler')

    server.heart = Heart()
    game_world.add_object(server.heart, 1)

    global font
    font = load_font('CookieRun Regular.TTF', 30)

    global time
    time = (get_time()//1)

    # server.coupon = Coupon()
    # game_world.add_object(server.coupon, 2)
    # game_world.add_collision_pairs(None, server.coupon, 'character:coupon')
    # game_world.add_collision_pairs(None, server.coupon, 'desk:coupon')

    global running
    running = True


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.03)

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    server.character.score += 5

    global time
    time = (get_time() // 1)

    if (time > 300):
        game_framework.change_state(ending_state)

    if (server.heart.heart_num < 0):
        game_framework.change_state(ending_state)

def draw():
    clear_canvas()
    draw_wolrd()
    update_canvas()

def draw_wolrd():
    for game_object in game_world.all_objects():
        game_object.draw()

    font.draw(50, 550, f'score : {int(server.character.score)}', (0, 0, 0))
    font.draw(730, 550, f'{int(server.heart.heart_num)}', (100, 0, 0))

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

def pause(): pass

def resume(): pass


def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

