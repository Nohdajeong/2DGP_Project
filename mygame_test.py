import pico2d
import game_framework

import main_state
import play_state
import title_state
import ending_state

pico2d.open_canvas()
game_framework.run(title_state)
# game_framework.run(main_state)
# game_framework.run(play_state)
# game_framework.run(ending_state)
pico2d.close_canvas()