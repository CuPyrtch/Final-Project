from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.rotation = 0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a", self.RotateLOn)
        SpaceGame.listenKeyEvent("keyup", "a", self.RotateLOff)
        SpaceGame.listenKeyEvent("keydown", "d", self.RotateROn)
        SpaceGame.listenKeyEvent("keyup", "d", self.RotateROff)
        self.fxcenter = self.fycenter = 0.5
        

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        # manage thrust animation
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
    def RotateLOn(self, event):
        self.vr = .01
    def RotateLOff(self, event):
        self.vr = 0
    def RotateROn(self, event):
        self.vr = -.01
    def RotateROff(self, event):
        self.vr = 0
    def thrustOn(self, event):
        self.thrust = 1
        self.vx = -math.sin(self.rotation)
        self.vy = -math.cos(self.rotation)
    def thrustOff(self, event):
        self.thrust = 0
        self.vx = 0
        self.vy = 0


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

        
myapp = SpaceGame()
myapp.run()
