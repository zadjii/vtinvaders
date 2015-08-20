import random
from drawing import *

__author__ = 'zadjii'


class GameScreen(object):
    _screen_width = 0
    _screen_height = 0
    
    def reset_grids(self, fg_grid, bg0_grid, bg1_grid):
        for y in range(0, self._screen_height):
            for x in range(0, self._screen_width):
                fg_grid[x][y] = (' ', 9, 9)
                bg0_grid[x][y] = (' ', 9, 9)
                bg1_grid[x][y] = (' ', 9, 9)

    def draw_borders(self, fg_grid, bg0_grid, bg1_grid):
        for x in range(0, len(bg1_grid)):
            bg1_grid[x][0] = ('X', WHITE, BLACK)
            bg1_grid[x][len(bg1_grid[x]) - 1] = ('X', WHITE, BLACK)
        for y in range(0, len(bg1_grid[0])):
            bg1_grid[0][y] = ('X', WHITE, BLACK)
            bg1_grid[len(bg1_grid) - 1][y] = ('X', WHITE, BLACK)

    def render(self, engine, fg_grid, bg0_grid, bg1_grid):

        self.reset_grids(fg_grid, bg0_grid, bg1_grid)
        self.draw_borders(fg_grid, bg0_grid, bg1_grid)

        for entity in engine.entities:
            entity.render(fg_grid, bg0_grid, bg1_grid)

        self.render_pt_2(engine, fg_grid, bg0_grid, bg1_grid)

    def render_pt_2(self, engine, fg_grid, bg0_grid, bg1_grid):
        do_reset()

        for y in range(0, self._screen_height):
            for x in range(0, self._screen_width):
                render_cell(fg_grid[x][y], bg0_grid[x][y], bg1_grid[x][y])
            if not y == self._screen_height-1:
                sys.stdout.write('\n')

    def set_screen_width_height(self, dimensions):
        self._screen_width = dimensions[0]
        self._screen_height = dimensions[1]