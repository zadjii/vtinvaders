import random
from drawing import *

__author__ = 'zadjii'


class GameScreen(object):
    

        # print 'this is the main game state'
    def render(self, engine, fg_grid, bg0_grid, bg1_grid):

        print \
        reset_sequence() \
        + move_to_sequence(5, 5) \
        + get_fg_sequence(RED) \
        +'@' \
        + move_to_sequence(10, 10) \
        + get_bg_sequence(random.randint(0, 9)) \
        + get_fg_sequence(random.randint(0, 9)) \
        + 'this is the main menu'