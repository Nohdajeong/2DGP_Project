from pico2d import *

floor = load_image('floor.png')
desk1 = load_image('desk_1.png')
desk2 = load_image('desk_2.png')
# book = load_image('book.png')

floor.draw_now(400, 30)
desk1.draw_now(420, 100)
desk2.draw_now(200, 170)

open_canvas()

bg = BackGround()
running = True

while running:
    handle_events()

    clear_canvas()
    bg.draw()
    update_canvas()

    delay(0.05)

close_canvas()