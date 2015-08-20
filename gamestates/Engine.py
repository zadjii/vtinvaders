import sys
from entities.Entity import Entity

__author__ = 'zadjii'
from Getch import getch

class Engine(object):

    entities = []
    effects = []

    def __init__(self):
        self.player = Entity()
        self.player.x = 10
        self.player.y = 10
        self.entities.append(self.player)

    def tick(self, delta):
        for entity in self.entities:
            entity.tick(self, delta)
        for effect in self.effects:
            effect.tick(self, delta)


    def process_inputs(self, delta):
        # pass
        # if sys.stdin.read():
        try:
            # input = sys.stdin.read(1)
            input = getch()
            if input == 'w':
                self.player.dy = -5.0
            elif input == 'a':
                self.player.dx = -5.0
            elif input == 's':
                self.player.dy =  5.0
            elif input == 'd':
                self.player.dx =  5.0
        except:
            pass
