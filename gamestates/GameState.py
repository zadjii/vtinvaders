__author__ = 'zadjii'


class GameState(object):
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