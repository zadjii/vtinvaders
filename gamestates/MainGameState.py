from Engine import Engine
from GameScreen import GameScreen
from GameState import GameState

__author__ = 'zadjii'


class MainGameState(GameState):
    engine = Engine()
    gamescreen = GameScreen()

    def render(self, fg_grid, bg0_grid, bg1_grid):
        # print 'this is the main game state'
        self.gamescreen.render(self.engine, fg_grid, bg0_grid, bg1_grid)


    def set_screen_width_height(self, dimensions):
        super(MainGameState, self).set_screen_width_height(dimensions)
        self.gamescreen.set_screen_width_height(dimensions)


    def process_inputs(self, delta):
        self.engine.process_inputs(delta)