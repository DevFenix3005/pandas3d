from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        
        
game = Game()
game.run()