from pico2d import *
import game_framework

import play_state

background = None
character = None
quiz = None
store = None

sx, sy = 400, 300
x, y = sx, sy
ax, ay = x, y

def enter():
    global background, character, quiz, store
    background = load_image('School_main.png')
    character = load_image('run_character.png')
    quiz = load_image('quiz.png')
    store = load_image('store.png')

def exit():
    global background, character, quiz, store
    del character
    del background
    del quiz
    del store

def update():
    pass

def handle_events():
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(play_state)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, event.y


    delay(0.01)

def draw():
    clear_canvas()
    background.draw(400, 220)
    character.draw(400, 300)
    quiz.draw(700, 500)
    store.draw(700, 400)
    update_canvas()



