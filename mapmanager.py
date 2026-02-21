class Mapmanager():
    
    def __init__(self):
        self.model = 'models/block.egg'
        self.texture  = 'textures/block.png'
        self.color = (0.2, 0.8, 0.2, 1)
        
        self.startNew()
        # self.addBlock((0, 10, 0))
        
    def startNew(self):
        self.land = render.attachNewNode("Land") 
    
    
    def addBlock(self, posicion):
        print(posicion)
        self.block = loader.loadModel(self.model)
        self.block_texture = loader.loadTexture(self.texture)
        self.block.setTexture(self.block_texture)
        self.block.setColor(self.color)
        self.block.setPos(posicion)
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                caracteres = line.split(' ')
                for z in caracteres:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1