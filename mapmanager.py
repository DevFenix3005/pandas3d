import pickle

class Mapmanager:
    def __init__(self):
        self.model = "models/block.egg"
        self.texture = "textures/block.png"
        self.colors = [
            (0.5, 0.3, 0.0, 1),
            (0.2, 0.2, 0.3, 1),
            (0.5, 0.5, 0.2, 1),
            (0.0, 0.6, 0.0, 1),
        ]

        self.startNew()
        # self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, posicion):
        self.block = loader.loadModel(self.model)
        self.block_texture = loader.loadTexture(self.texture)
        self.block.setTexture(self.block_texture)

        self.color = self.getColor(posicion[2])
        self.block.setColor(self.color)
        self.block.setPos(posicion)
        self.block.reparentTo(self.land)
        self.block.setTag("at", str(posicion))

    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def buildBlock(self, pos):
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new)

    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(
            position
        )  # las coordenadas del bloque más alto desocupado frente al jugador
        pos = x, y, z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def getColor(self, z):
        len_colors = len(self.colors)
        if z < len_colors:
            return self.colors[z]
        else:
            return self.colors[len_colors - 1]

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                caracteres = line.split(" ")
                for z in caracteres:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True

    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)

    def saveMap(self):
        blocks = self.land.getChildren()
        with open("my_map.dat", "wb") as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)

    def loadMap(self):
        self.clear()
        with open("my_map.dat", "rb") as fin:
            length = pickle.load(fin)
            for i in range(length):
                pos = pickle.load(fin)
                self.addBlock(pos)