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
