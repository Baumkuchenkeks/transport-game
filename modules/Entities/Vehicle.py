from __future__ import annotations
import pygame
import math
from .Position import Position
from .Storage import Storage
from ..Utils import Utility
# from ..App import App


class Vehicle(pygame.sprite.Sprite):
    weight: float
    # position: Position
    directionalSpeed: list[int] #[int,int]
    acceleration: float
    rotationSpeed: int
    rotationImage: pygame.Surface
    rotationRect: pygame.Rect
    direction: int
    speed: float
    maxSpeed: float
    isFlying: bool
    storage: Storage

    def __init__(self: Vehicle, weight: float, acceleration: int, maxSpeed: float, isFlying: bool, maxStorage: int):
        pygame.sprite.Sprite.__init__(self)
        if(isFlying):
            self.image = self.rotationImage = pygame.image.load("data/images/heli.png")
        else:
            self.image = self.rotationImage = pygame.image.load("data/images/truck-small.png")
        self.rect = self.rotationRect = self.image.get_rect()
        self.rect = self.rotationRect = self.rect.move(1580, 850)
        self.direction = -45
        self.setRotation()
    
        self.weight = weight
        self.acceleration = acceleration
        self.maxSpeed = maxSpeed
        self.isFlying = isFlying
        self.storage = Storage(maxStorage)
        self.rotationSpeed = 4
        self.speed = 0

    def update(self: Vehicle):
        rad = math.radians(self.direction)
        x = math.cos(rad) * self.speed
        y = math.sin(rad) * self.speed
        self.rect = self.rect.move(-x, y)
        self.rotationRect = self.rotationRect.move(-x, y)

    def getSpeed(self: Vehicle):
        return self.speed

    def getRect(self: Vehicle):
        return self.rect

    def getStorage(self: Vehicle):
        return self.storage

    def accelerate(self: Vehicle):
        self.speed = min(self.speed + self.acceleration, self.maxSpeed)

    def decelerate(self: Vehicle):
        self.speed = max(self.speed - self.acceleration / 2, 0)

    def brake(self: Vehicle):
        self.speed = max(self.speed - self.acceleration * 4, 0)

    def turnRight(self: Vehicle):
        self.rotate()
    
    def turnLeft(self: Vehicle):
        self.rotate(left = True)

    def rotate(self: Vehicle, left: bool = False):
        if left:
            self.direction += self.rotationSpeed
        else:
            self.direction -= self.rotationSpeed
        self.setRotation()

    def setRotation(self:Vehicle):
        utility = Utility()
        rotation = utility.rotateCenter(self.rotationImage, self.rotationRect.topleft, self.direction)
        self.image = rotation[0]
        self.rect = rotation[1]

    def moveTowards(self: Vehicle, sprite: pygame.sprite.Sprite, app):
        # self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > app.width:
            self.directionalSpeed[0] = -self.directionalSpeed[0]
        if self.rect.top < 0 or self.rect.bottom > app.height:
            self.directionalSpeed[1] = -self.directionalSpeed[1]