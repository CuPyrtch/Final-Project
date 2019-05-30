from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/player1.png", 
        Frame(119,90,50,50), 3, 'vertical')
        
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.rotation = 0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "a", self.RotateLOn)
        SpaceGame.listenKeyEvent("keyup", "a", self.RotateLOff)
        SpaceGame.listenKeyEvent("keydown", "d", self.RotateROn)
        SpaceGame.listenKeyEvent("keyup", "d", self.RotateROff)
        

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
    def RotateLOn(self, event):
        self.vx = -2
    def RotateLOff(self, event):
        self.vx = 0
    def RotateROn(self, event):
        self.vx = 2
    def RotateROff(self, event):
        self.vx = 0


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
        SpaceShip((500,470))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

        
myapp = SpaceGame()
myapp.run()