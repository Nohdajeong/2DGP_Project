from pico2d import *
import game_framework

import play_state
import server
import time

image = None
tip = None
num = 0

def enter():
    global image, tip
    image = load_image('resource/stop_select.png')
    tip = load_image('resource/tip.png')

def exit():
    global image, tip
    del image
    del tip

def update():
    pass

def pause():
    pass

def resume():
    pass

def draw():
    clear_canvas()
    play_state.draw_wolrd()
    image.draw(400, 300)

    if num % 2 == 0:
        image.draw(400, 300)

    if num % 2 == 1:
        tip.draw(400, 300)

    update_canvas()

def handle_events():
    global num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_F1:
                    server.character.score = 0
                    server.heart.heart_num = 3
                    game_framework.pop_state()
                case pico2d.SDLK_F2:
                    game_framework.pop_state()
                case pico2d.SDLK_F3:
                    num += 1



def test_self():
    import run_stop_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(run_stop_state)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()