import pico2d
import game_framework

import title_state
import play_state

pico2d.open_canvas()
# game_framework.run(title_state)
game_framework.run(play_state)
pico2d.close_canvas()