from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
r = input("What do you want the difficulty to be? 1 = Easy, 2 = Medium, 3 = Extreme!")

if r == "1":
    f = .25
    print("Easy mode selected!")
elif r == "2":
    f = .5
    print("Medium mode selected!")
elif r == "3":
    f = 1
    print("Extreme mode selected!!!")
else:
    f = .75
    print("No input given, defaulted to Medium")

white = Color(0xfffafa, 1.0)
thinline = LineStyle(1, white)
rectangle = RectangleAsset(1100, 0, thinline, white)
bottom = Sprite(rectangle, (0, 510))
top = Sprite(rectangle, (0, 0))

class Blast(Sprite):
    asset = ImageAsset("images/player1.png", Frame(134,30,18,30), 1, 'vertical')
    collisionasset = CircleAsset(5)
    
    def __init__(self, app):
        super().__init__(Blast.asset,  (0,0))
        self.visible = False
        self.firing = False
        self.time = 0
        self.vy = 0
        self.vx = 0
        self.vr = 0
        
    def shoot(self, position, velocity, time):
        self.position = position
        self.vx = 0
        self.vy = -8
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
        self.fxcenter = .31
        SpaceShooter.listenKeyEvent("keydown", "a", self.LOn)
        SpaceShooter.listenKeyEvent("keyup", "a", self.LOff)
        SpaceShooter.listenKeyEvent("keydown", "d", self.ROn)
        SpaceShooter.listenKeyEvent("keyup", "d", self.ROff)
        

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
    def LOn(self, event):
        self.vx = -5
    def LOff(self, event):
        self.vx = 0
    def ROn(self, event):
        self.vx = 5
    def ROff(self, event):
        self.vx = 0

class Enemy(Sprite):
    asset = ImageAsset("images/191-1916209_space-invaders-sprites.png", 
        Frame(140, 200,50,50), 1, 'vertical')
    collisionasset = CircleAsset(40)
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.vx = 0
        self.vy = f
        self.vr = 0
        self.rotation = 0
        self.thrust = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        blast = self.collidingWithSprites(Blast)
        if blast:
            self.destroy()
            blast[0].destroy()


class SpaceShooter(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        line = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, line, black)
        bg = Sprite(bg_asset, (0,0))
        self.shooter = Shooter((500,450))
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
   
        #self.blast = Blast(self)
        SpaceShooter.listenKeyEvent("keydown", "space", self.ShootOn)

    def ShootOn(self, event):
        self.blast = Blast(self)
        self.blast.shoot(self.shooter.position,430,0)

        
    def step(self):
        for ship in self.getSpritesbyClass(Blast):
            ship.step()
        for ship in self.getSpritesbyClass(Shooter):
            ship.step()
        for ship in self.getSpritesbyClass(Enemy):
            ship.step()


        
myapp = SpaceShooter()
myapp.run()