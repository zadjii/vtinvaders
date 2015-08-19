from datetime import datetime
# from datetime import time

from gamestates.MainMenuState import MainMenuState
from gamestates.MainGameState import MainGameState

__author__ = 'zadjii'


MAIN_MENU_STATE_INDEX = 0
MAIN_GAME_STATE_INDEX = 1

main_menu_state = MainMenuState()
main_game_state = MainGameState()

class Game(object):




    game_states = {
        MAIN_MENU_STATE_INDEX:main_menu_state
        ,MAIN_GAME_STATE_INDEX:main_game_state
    }

    current_state_index = MAIN_MENU_STATE_INDEX
    exit_requested = False

    TIME_INCREMENT = (1.0/60.0)

    screen_width = 0
    screen_height = 0
    screen_initialized = False
    fg_buffer = []
    bg0_buffer = []
    bg1_buffer = []

    def __init__(self):
        self.last_time = datetime.utcnow()
        self.time_accumulator = 0.0
        self.total_time = 0.0

    def run(self):
        last_sec = 0
        while not self.exit_requested:
            curr_time = datetime.utcnow()
            frame_time = curr_time - self.last_time
            self.last_time = curr_time
            # print self.time_accumulator
            frame_time = frame_time.total_seconds()
            # print frame_time
            self.time_accumulator += frame_time
            current_state = self.game_states[self.current_state_index]
            while self.time_accumulator > self.TIME_INCREMENT:
                delta = self.TIME_INCREMENT
                current_state.process_inputs(delta)
                current_state.tick(delta)
                current_state.render( self.fg_buffer, self.bg0_buffer, self.bg1_buffer)
                self.time_accumulator -= delta
                self.total_time += delta
            if int(self.total_time) > last_sec:
            #     print frame_time, self.total_time
            #     current_state.render( self.fg_buffer, self.bg0_buffer, self.bg1_buffer)
                last_sec = int(self.total_time)
            # time.sleep(.1)
            if self.total_time > 3:
                current_state.switch_to(MAIN_GAME_STATE_INDEX)
                main_game_state.switch_from(self.current_state_index)
                self.current_state_index = MAIN_GAME_STATE_INDEX
            if self.total_time > 10:
                request_exit()
    def init_screen(self):
        #todo get screen w,h
        #todo set up fg,bg0/1 buffers.
        self.screen_initialized = True




game = Game()

def request_exit():
    global game
    game.exit_requested = True


if __name__ == '__main__':

    game.run()

    # if there weren't any args, print the usage and return
    # if len(sys.argv) < 2:
    #     usage()
    #     sys.exit(0)
    #
    # command = sys.argv[1]
    #
    # selected = commands.get(command, usage)
    # selected(sys.argv[2:])
    # sys.exit(0)