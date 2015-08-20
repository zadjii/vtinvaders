import drawing

__author__ = 'zadjii'

class Entity(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.w = 0
        self.h = 0

    def tick(self, delta):
        self.x += delta * self.dx
        self.y += delta * self.dy

    def render(self, fg_grid, bg0_grid, bg1_grid):
        fg_grid[self.intx()][self.inty()] = ('@', drawing.BLUE, drawing.CLEAR)

    def intx(self):
        return int(self.x)

    def inty(self):
        return int(self.y)

