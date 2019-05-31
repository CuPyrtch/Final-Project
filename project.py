from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class Blast(Sprite):
    asset = ImageAsset("images/player1.png", Frame(119,90,50,50), 1, 'vertical')
    collisionasset = CircleAsset(4)
    
    def __init__(self, app):
        super().__init__(Bullet.asset, Bullet.collisionasset, (0,0), (0,0))
        self.visible = False
        self.firing = False
        self.time = 0
        
    def shoot(self, position, velocity, time):
        self.position = position
        self.vx = velocity[0]
        self.vy = velocity[1]
        self.time = time
        self.visible = True
        self.firing = True
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr

class Shooter(Sprite):
    asset = ImageAsset("images/player1.png", 
        Frame(119,90,50,50), 1, 'vertical')
        
    def __init__(self, position):
        super().__init__(Shooter.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.rotation = 0
        self.thrust = 0
        SpaceShooter.listenKeyEvent("keydown", "a", self.RotateLOn)
        SpaceShooter.listenKeyEvent("keyup", "a", self.RotateLOff)
        SpaceShooter.listenKeyEvent("keydown", "d", self.RotateROn)
        SpaceShooter.listenKeyEvent("keyup", "d", self.RotateROff)
        SpaceShooter.listenKeyEvent("keydown", "space", self.ShootOn)
        SpaceShooter.listenKeyEvent("keyup", "space", self.ShootOff)
        

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
    def ShootOn(self, event):
        shoot = True
    def ShootOff(self, event):
        shoot = False

class Enemy(Sprite):
    asset = ImageAsset("images/191-1916209_space-invaders-sprites.png", 
        Frame(140, 200,50,50), 1, 'vertical')
    collisionasset = CircleAsset(40)
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.vx = 0
        self.vy = 1
        self.vr = 0
        self.rotation = 0
        self.thrust = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr

class SpaceShooter(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Shooter((500,470))
        Enemy((100, 50))
   
    def step(self):
        for ship in self.getSpritesbyClass(Enemy):
            ship.step()

    def step(self):
        for ship in self.getSpritesbyClass(Shooter):
            ship.step()

        
myapp = SpaceShooter()
myapp.run()