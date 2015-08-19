import random
from GameState import GameState
from drawing import *
__author__ = 'zadjii'


class MainMenuState(GameState):
    def render(self, fg_grid, bg0_grid, bg1_grid):

        print \
            reset_sequence() \
            + get_bg_sequence(random.randint(0, 9)) \
            + get_fg_sequence(random.randint(0, 9)) \
            + 'this is the main menu'
        # print get_bg_bold_sequence(random.randint(0, 9)) + 'this is the main menu'
        # pass