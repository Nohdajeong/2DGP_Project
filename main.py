import pico2d
import play_state
import main_state

pico2d.open_canvas()
states = [main_state, play_state]
for state in states:
    state.enter()

    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()

pico2d.close_canvas()