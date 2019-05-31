from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
r = input("What do you want the difficulty to be? .5 = Easy, 1 = Medium, 2 = Extreme!")

class Blast(Sprite):
    asset = ImageAsset("images/player1.png", Frame(119,90,50,50), 1, 'vertical')
    collisionasset = CircleAsset(4)
    
    def __init__(self, app):
        super().__init__(Blast.asset, Blast.collisionasset, (0,0), (0,0))
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
        self.vx = -3
    def RotateLOff(self, event):
        self.vx = 0
    def RotateROn(self, event):
        self.vx = 3
    def RotateROff(self, event):
        self.vx = 0
    def ShootOn(self, event):
        Blast.shoot(self.position,450,Blast.y,Blast.time)
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
        Shooter((500,450))
        Enemy((40, 10))
        Enemy((130, 10))
        Enemy((220, 10))
        Enemy((310, 10))
        Enemy((400, 10))
        Enemy((490, 10))
        Enemy((580, 10))
        Enemy((670, 10))
        Enemy((760, 10))
        Enemy((850, 10))
        Enemy((940, 10))
        
        Enemy((40, 80))
        Enemy((130, 80))
        Enemy((220, 80))
        Enemy((310, 80))
        Enemy((400, 80))
        Enemy((490, 80))
        Enemy((580, 80))
        Enemy((670, 80))
        Enemy((760, 80))
        Enemy((850, 80))
        Enemy((940, 80))
   
    def step(self):
        for ship in self.getSpritesbyClass(Enemy):
            ship.step()

    def step(self):
        for ship in self.getSpritesbyClass(Shooter):
            ship.step()

        
myapp = SpaceShooter()
myapp.run()