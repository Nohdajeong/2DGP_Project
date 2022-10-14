# 첫 구현 : 오브젝트 & 맵 배경

import pico2d
import play_state

start_state = play_state

pico2d.open_canvas()
start_state.enter()

while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()
    pico2d.delay(0.05)

start_state.exit()

pico2d.close_canvas()