__author__ = 'zadjii'


class Engine(object):

    entities = []
    effects = []


    def tick(self, delta):
        for entity in self.entities:
            entity.tick(self, delta)
        for effect in self.effects:
            effect.tick(self, delta)

