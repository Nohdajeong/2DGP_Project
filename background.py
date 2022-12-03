from pico2d import *

import server

class BackGround:
    def __init__(self):
        self.image = load_image('School_stage1.png')
        self.bgm = load_music('run_music.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def __getstate__(self):
        state = {}
        return state

    def __setstate__(self, state):
        self.__init__()

    def draw(self):
        self.image.draw(400, 220)

    def update(self):
        pass

    def handle_event(self, event):
        pass
