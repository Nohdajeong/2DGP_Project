from pico2d import *
import game_framework
import title_state
import play_state
import server

score = 0
endimage = None
font1 = None
font2 = None
bgm = None

def enter():
    global endimage, font1, font2, score, bgm
    endimage = load_image('resource/end.png')
    font1 = load_font('CookieRun Regular.TTF', 80)
    font2 = load_font('CookieRun Regular.TTF', 40)
    score = server.character.score

    bgm = load_music('resource/r_score.ogg')
    bgm.set_volume(32)
    bgm.play(1)


def exit():
    global endimage
    del endimage

def update(): pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_RETURN:
                    game_framework.change_state(play_state)

def draw():
    global score
    clear_canvas()
    endimage.draw(400, 300)
    font1.draw(300, 380, f'{int(score)}', (255, 255, 255))
    if score > 0 :
        font2.draw(300, 300, f'coin : {int(score // 100)}', (255, 255, 255))
    else:
        font2.draw(300, 300, f'coin : 0', (255, 255, 255))
    update_canvas()

def test_self():
    import ending_state
    pico2d.open_canvas()
    game_framework.fill_states(play_state)
    game_framework.run(ending_state)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()