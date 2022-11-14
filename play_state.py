from pico2d import *
import game_framework
import game_world

import run_stop_state

from character import Character
from floor import Floor
from background import BackGround
from desk import Desk1, Desk2
from ruler import Ruler
from heart import Heart

# back
background = None
floor = None

# object
desk1 = None
desk2 = None
ruler = None

# character
character = None
running = True
heart = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(run_stop_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            if Heart.heart1 == None:
                Heart.heart1 = load_image('heart.png')
                if Heart.heart2 == None:
                    Heart.heart2 = load_image('heart.png')
                    if Heart.heart3 == None:
                        Heart.heart3 = load_image('heart.png')
            print('skill 1')
        else:
            character.handle_event(event)


# 초기화
def enter():
    # back
    global background, floor
    background = BackGround()
    floor = Floor()
    game_world.add_object(background, 0)
    game_world.add_object(floor, 0)

    # object
    global desk1, desk2, ruler
    desk1 = Desk1()
    desk2 = Desk2()
    ruler = Ruler()
    game_world.add_object(desk1, 1)
    game_world.add_object(desk2, 1)
    game_world.add_object(ruler, 1)

    # character
    global character
    character = Character()
    game_world.add_object(character, 1)

    global heart
    heart = Heart()
    game_world.add_object(heart, 1)

    global running
    running = True

# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(character, desk1):
        print("Collision character:desk1")

    if collide(character, desk2):
        print("Collision character:desk2")


def draw():
    clear_canvas()
    draw_wolrd()
    update_canvas()

def draw_wolrd():
    for game_object in game_world.all_objects():
        game_object.draw()

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

