from __future__ import annotations
import pygame
import math
from .Storage import Storage
from ..Utils import Utility


class Vehicle(pygame.sprite.Sprite):
    weight: float
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
    gasUsage: float
    fillRate: int

    def __init__(self: Vehicle, weight: float, acceleration: float, maxSpeed: float, isFlying: bool, maxStorage: int):
        """creates a new Vehicle"""
        pygame.sprite.Sprite.__init__(self)
        if(isFlying):
            self.image = self.rotationImage = pygame.image.load("data/images/heli.png")
            self.rect = self.rotationRect = self.image.get_rect()
            self.fillRate = 10
        else:
            self.image = self.rotationImage = pygame.image.load("data/images/truck.png")
            self.rect = self.rotationRect = self.image.get_rect()
            self.fillRate = 5
        self.direction = 315
        self.setRotation()
    
        self.weight = weight
        self.acceleration = acceleration
        self.maxSpeed = maxSpeed
        self.isFlying = isFlying
        self.storage = Storage(maxStorage)
        self.rotationSpeed = 4
        self.speed = 0
        self.gas = 180
        self.maxGas = 180
        self.gasUsage = 0.5

    def update(self: Vehicle):
        """Updates the needed parameters. Call in the main loop.
        Moves the Vehicle based on direction and speed.
        Updates gas tank
        """
        rad = math.radians(self.direction)
        x = math.cos(rad) * self.speed
        y = math.sin(rad) * self.speed
        self.rect = self.rect.move(-x, y)
        self.rotationRect = self.rotationRect.move(-x, y)
        self.useGas(self.gasUsage * self.acceleration)
        self.gasUsage = 0.5

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
        """Reduces vehicles gas by the given amount."""
        self.gas -= amount

    def getMaxGas(self: Vehicle)-> float:
        return self.maxGas
    
    def getDirection(self: Vehicle) -> int:
        return self.direction
    
    def getFillRate(self:  Vehicle) -> int:
        return self.fillRate

    def accelerate(self: Vehicle):
        """Increases vehicles speed up to a maximum.
        If gas is empty vehicle can't accelerate.
        """
        self.gasUsage += 0.5
        if(self.gas > 0):
            self.speed = min(self.speed + self.acceleration, self.maxSpeed)
        else:
            self.decelerate

    def decelerate(self: Vehicle):
        """Reduces vehicles speed down to 0."""
        self.gasUsage -= 0.5
        self.speed = max(self.speed - self.acceleration / 2, 0)

    def brake(self: Vehicle):
        """Reduces vehicles speed down to 0.
        Faster than decelerate.
        """
        self.speed = max(self.speed - self.acceleration * 4, 0)

    def turnRight(self: Vehicle, max: int = None):
        """Rotates vehicle to the right side.
        Uses Vehicle.rotate()
        """
        self.rotate(max = max)
    
    def turnLeft(self: Vehicle, max: int = None):
        """Rotates vehicle to the left side.
        Uses Vehicle.rotate()
        """
        self.rotate(left = True, max = max)

    def rotate(self: Vehicle, left: bool = False, max: int = None):
        """Rotates the vehicle by manipulating its direction."""
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
        """Rotate vehicles image and rectangle around the center.
        Uses Utility.rotateCenter
        """
        utility = Utility()
        rotation = utility.rotateCenter(self.rotationImage, self.rotationRect.topleft, self.direction)
        self.image = rotation[0]
        self.rect = rotation[1]