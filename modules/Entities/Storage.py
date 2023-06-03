from __future__ import annotations
import pygame

class Storage(pygame.sprite.Sprite):
    maxAmount: int
    amount: int

    def __init__(self: Storage, maxAmount: int, amount: int = 0, image: pygame.Surface = None):
        """creates a new Storage"""
        if image:
            pygame.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect()
        self.amount = amount
        self.maxAmount = maxAmount

    def getRect(self: Storage):
        return self.rect

    def getAmount(self: Storage):
        return self.amount

    def getMaxAmount(self: Storage):
        return self.maxAmount

    def fill(self: Storage, amount: int)-> int:
        """fills the storage by a given amount
        returns 0 or the remaining amount if too full
        """
        if(self.amount + amount <= self.maxAmount):
            self.amount += amount
            return 0
        else:
            diff = self.maxAmount - self.amount
            self.amount = self.maxAmount
            return diff

    #takes a given amount out of the storage
    #returns the taken amount
    def empty(self: Storage, amount: int)-> int:
        """takes a given amount out of the storage
        returns the taken amount
        """
        if(self.amount - amount >= 0):
            self.amount -= amount
            return amount
        else:
            # insert error here
            given = self.amount
            self.amount = 0
            return given
