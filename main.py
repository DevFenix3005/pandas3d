from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        self.hero = Hero((0, 0, 1),self.land)
        
game = Game()
game.run()