import pico2d
import game_framework

import main_state
import play_state
import shop_state
import title_state

pico2d.open_canvas()
# game_framework.run(title_state)
# game_framework.run(main_state)
game_framework.run(play_state)
pico2d.close_canvas()