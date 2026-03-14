from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        x, y = self.land.loadLand("land.txt")
        print("Tamaño del mapa: {} {}".format(x, y))
        self.hero = Hero((x // 2, y // 2, 1), self.land)


game = Game()
game.run()
