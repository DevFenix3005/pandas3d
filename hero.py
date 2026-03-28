def check_dir(angle):
    """devuelve cambios redondeados en las coordenadas X, Y
    correspondientes al movimiento hacia el ángulo.
    La coordenada Y disminuye si el personaje está mirando a un ángulo 0,
    y aumenta cuando está mirando a un ángulo de 180.
    La coordenada X aumenta si el personaje está mirando a un ángulo de 90,
    y disminuye cuando está mirando a un ángulo de 270.
        de   0 a 20  -> Y - 1
        de  25 a 65  -> X + 1, Y - 1
        de  70 a 110 -> X + 1
        de 115 a 155 -> X + 1, Y + 1
        de 160 a 200 -> Y + 1
        de 205 a 245 -> X - 1, Y + 1
        de 250 a 290 -> X - 1
        de 290 a 335 -> X - 1, Y - 1
        de 340       -> Y - 1"""
    if angle >= 0 and angle <= 20:
        return (0, -1)
    elif angle <= 65:
        return (1, -1)
    elif angle <= 110:
        return (1, 0)
    elif angle <= 155:
        return (1, 1)
    elif angle <= 200:
        return (0, 1)
    elif angle <= 245:
        return (-1, 1)
    elif angle <= 290:
        return (-1, 0)
    elif angle <= 335:
        return (-1, -1)
    else:
        return (0, -1)


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = False

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        x = self.hero.getX()
        y = self.hero.getY()
        z = self.hero.getZ()
        base.mouseInterfaceNode.setPos((-x, -y, -z - 3))
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def accept_events(self):
        base.accept("c", self.change_view)
        base.accept("n", self.turn_left)
        base.accept("n" + "-repeat", self.turn_left)
        base.accept("m", self.turn_right)
        base.accept("m" + "-repeat", self.turn_right)

        base.accept("s", self.back)
        base.accept("s" + "-repeat", self.back)
        base.accept("w", self.forward)
        base.accept("w" + "-repeat", self.forward)

        base.accept("a", self.left)
        base.accept("a" + "-repeat", self.left)
        base.accept("d", self.right)
        base.accept("d" + "-repeat", self.right)

        base.accept("e", self.up)
        base.accept("e" + "-repeat", self.up)

        base.accept("q", self.down)
        base.accept("q" + "-repeat", self.down)

        base.accept("z", self.change_mode)

        base.accept("b", self.build)
        base.accept("v", self.destroy)

        base.accept("k", self.land.saveMap)
        base.accept("l", self.land.loadMap)

    def change_view(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        current_heading = self.hero.getH()
        current_heading = current_heading + 5
        self.hero.setH(current_heading % 360)

    def turn_right(self):
        current_heading = self.hero.getH()
        current_heading = current_heading - 5
        self.hero.setH(current_heading % 360)

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = check_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def fly(self, value):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + value)

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def up(self):
        self.fly(1)

    def down(self):
        self.fly(-1)

    def change_mode(self):
        if self.mode:
            self.mode = False
            self.hero.setZ(1)
        else:
            self.mode = True

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)
