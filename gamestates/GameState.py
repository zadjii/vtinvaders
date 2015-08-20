__author__ = 'zadjii'


class GameState(object):
    _screen_width = 0
    _screen_height = 0
    def tick(self, delta):
        pass

    def render(self, fg_grid, bg0_grid, bg1_grid):
        pass

    def switch_to(self, to_state):
        pass

    def switch_from(self, from_state):
        pass

    def process_inputs(self, delta):
        pass

    def set_screen_width_height(self, dimensions):
        self._screen_width = dimensions[0]
        self._screen_height = dimensions[1]