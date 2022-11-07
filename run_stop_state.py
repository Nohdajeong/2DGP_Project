import pico2d

import game_framework
from pico2d import *
import play_state

image = None

def enter():
    global image
    image = load_image('stop_select.png')

def exit():
    global image
    del image

def update():
    pass

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
                    game_framework.pop_state()


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