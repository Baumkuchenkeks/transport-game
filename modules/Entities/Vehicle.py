from __future__ import annotations
import pygame
from .Position import Position
from .Storage import Storage
from ..Constants import Constants
# from ..App import App


class Vehicle(pygame.sprite.Sprite):
    weight: float
    # position: Position
    speed: list[int] #[int,int]
    acceleration: int   
    direction: int #0-7
    maxSpeed: float
    isFlying: bool
    storage: Storage

    def __init__(self: Vehicle, weight: float, acceleration: int, maxSpeed: float, isFlying: bool, maxStorage: int, speed: list[int] = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        if(isFlying):
            width = 50
            height = 50
            self.image = pygame.Surface([width, height])
            self.image.fill(Constants().getColor("GREEN"))
        else:
            width = 100
            height = 50
            self.image = pygame.Surface([width, height])
            self.image.fill(Constants().getColor("RED"))
        self.rect = self.image.get_rect()
    
        self.weight = weight
        self.acceleration = acceleration
        self.maxSpeed = maxSpeed
        self.speed = [0,0]
        self.isFlying = isFlying
        self.storage = Storage(maxStorage)
        self.speed = speed
        self.direction = 2

    def update(self: Vehicle):
        self.rect = self.rect.move(self.speed)

    def accelerate(self: Vehicle):
        print(self.speed)
        speed = self.speed[0] * self.speed[1]
        if(speed >= self.maxSpeed):
            return
        else:
            #accelerate based on direction
            if(self.direction == 0):
                if(self.speed[0] > 1 or self.speed[0] < -1):
                    self.speed[0]= round(self.speed[0] / 2)
                else:
                    self.speed[0]= 0
                self.speed[1]= self.speed[1] + self.acceleration
            elif(self.direction == 1):
                self.speed[0] = self.speed[0] + round(self.acceleration/2)
                self.speed[1] = self.speed[1] + round(self.acceleration/2)
            elif(self.direction == 2):
                if(self.speed[1] > 1 or self.speed[1] < -1):
                    self.speed[1]= round(self.speed[1] / 2)
                else:
                    self.speed[1]= 0
                self.speed[0]= self.speed[0] + self.acceleration
            elif(self.direction == 3):
                self.speed[0] = self.speed[0] + round(self.acceleration/2)
                self.speed[1] = self.speed[1] - round(self.acceleration/2)
            elif(self.direction == 4):
                if(self.speed[0] > 1 or self.speed[0] < -1):
                    self.speed[0]= round(self.speed[0] / 2)
                else:
                    self.speed[0]= 0
                self.speed[1]= self.speed[1] - self.acceleration
            elif(self.direction == 5):
                self.speed[0] = self.speed[0] - round(self.acceleration/2)
                self.speed[1] = self.speed[1] - round(self.acceleration/2)
            elif(self.direction == 6):
                if(self.speed[1] > 1 or self.speed[1] < -1):
                    self.speed[1]= round(self.speed[1] / 2)
                else:
                    self.speed[1]= 0
                self.speed[0]= self.speed[0] - self.acceleration
            elif(self.direction == 7):
                self.speed[0] = self.speed[0] - round(self.acceleration/2)
                self.speed[1] = self.speed[1] + round(self.acceleration/2)
            else:
                print("ERROR: DIRECTION INVALID")

    def decelerate(self: Vehicle):
        deceleration = self.acceleration*2
        if(self.speed[0] > 1):
            if(self.speed[0] > deceleration):
                self.speed[0] = self.speed[0] - deceleration
            else:
                self.speed[0] = 0
        elif(self.speed[0] < 1):
            if(self.speed[0] < (deceleration*-1)):
                self.speed[0] = self.speed[0] + deceleration
            else:
                self.speed[0] = 0
        else:
            self.speed[0] = 0
        
        if(self.speed[1] > 1):
            if(self.speed[1] > deceleration):
                self.speed[1] = self.speed[1] - deceleration
            else:
                self.speed[1] = 0
        elif(self.speed[1] < 1):
            if(self.speed[1] < (deceleration*-1)):
                self.speed[1] = self.speed[1] + deceleration
            else:
                self.speed[1] = 0
        else:
            self.speed[1] = 0

    def turnRight(self: Vehicle):
        if(self.direction == 7):
            self.direction = 0
        else:
            self.direction += 1
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
    
    def turnLeft(self: Vehicle):
        if(self.direction == 0):
            self.direction = 7
        else:
            self.direction -= 1
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

    def moveTowards(self: Vehicle, sprite: pygame.sprite.Sprite, app):
        # self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > app.width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > app.height:
            self.speed[1] = -self.speed[1]