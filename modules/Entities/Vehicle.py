from __future__ import annotations
import pygame
import math
from .Position import Position
from .Storage import Storage
from ..Utils import Utility


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
    gas: float
    maxGas: float
    gasUsage: int

    def __init__(self: Vehicle, weight: float, acceleration: float, maxSpeed: float, isFlying: bool, maxStorage: int):
        pygame.sprite.Sprite.__init__(self)
        if(isFlying):
            self.image = self.rotationImage = pygame.image.load("data/images/heli.png")
            self.rect = self.rotationRect = self.image.get_rect()
        else:
            self.image = self.rotationImage = pygame.image.load("data/images/truck-small.png")
            self.rect = self.rotationRect = self.image.get_rect()
        self.direction = 315
        self.setRotation()
    
        self.weight = weight
        self.acceleration = acceleration
        self.maxSpeed = maxSpeed
        self.isFlying = isFlying
        self.storage = Storage(maxStorage)
        self.rotationSpeed = 4
        self.speed = 0
        self.gas = 5000
        self.maxGas = 5000
        self.gasUsage = 3

    def update(self: Vehicle):
        rad = math.radians(self.direction)
        x = math.cos(rad) * self.speed
        y = math.sin(rad) * self.speed
        self.rect = self.rect.move(-x, y)
        self.rotationRect = self.rotationRect.move(-x, y)
        self.useGas(self.gasUsage * self.acceleration)
        self.gasUsage = 3

    def getSpeed(self: Vehicle)-> float:
        return self.speed

    def getRect(self: Vehicle)-> pygame.rect.Rect:
        return self.rect

    def getStorage(self: Vehicle)-> Storage:
        return self.storage

    def getGas(self: Vehicle)-> float:
        return self.gas

    def setGas(self: Vehicle, gas: float):
        self.gas = gas

    def useGas(self: Vehicle, amount: float):
        self.gas -= amount

    def getMaxGas(self: Vehicle)-> float:
        return self.maxGas
    
    def getDirection(self: Vehicle) -> int:
        return self.direction

    def accelerate(self: Vehicle):
        self.gasUsage += 3
        if(self.gas > 0):
            self.speed = min(self.speed + self.acceleration, self.maxSpeed)
        else:
            self.decelerate

    def decelerate(self: Vehicle):
        self.gasUsage -= 3
        self.speed = max(self.speed - self.acceleration / 2, 0)

    def brake(self: Vehicle):
        self.speed = max(self.speed - self.acceleration * 4, 0)

    def turnRight(self: Vehicle, max: int = None):
        self.rotate(max = max)
    
    def turnLeft(self: Vehicle, max: int = None):
        self.rotate(left = True, max = max)

    def rotate(self: Vehicle, left: bool = False, max: int = None):
        if left:
            if max and max < self.rotationSpeed:
                self.direction += max
            else:
                self.direction += self.rotationSpeed
        else:
            if max and max < self.rotationSpeed:
                self.direction -= max
            else:
                self.direction -= self.rotationSpeed
        if self.direction >= 360:
            self.direction -= 360
        elif self.direction <= 0:
            self.direction += 360
        self.setRotation()

    def setRotation(self:Vehicle):
        utility = Utility()
        rotation = utility.rotateCenter(self.rotationImage, self.rotationRect.topleft, self.direction)
        self.image = rotation[0]
        self.rect = rotation[1]