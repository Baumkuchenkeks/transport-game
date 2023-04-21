from __future__ import annotations

class Storage:
    maxAmount: int
    amount: int

    def __init__(self: Storage, maxAmount: int, amount: int = 0):
        self.amount = amount
        self.maxAmount = maxAmount

    #fills the storage by a given amount
    #returns 0 or the remaining amount if too full
    def fill(self: Storage, amount: int)-> int:
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
        if(self.amount - amount >= 0):
            self.amount -= amount
            return amount
        else:
            # insert error here
            given = self.amount
            self.amount = 0
            return given
