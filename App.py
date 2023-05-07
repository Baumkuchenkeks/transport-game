from __future__ import annotations
import typing
import pygame
from pygame.locals import *
from modules.Utils import Utility
from modules.VehicleAi import VehicleAi
from modules.Entities.Vehicle import Vehicle
from modules.Entities.Storage import Storage
from modules.Entities.Text import Text

class App:
    TITLE = "transport-game"
    VERSION = "0.01-07042023"

    MINESTORAGE = 3000
    FPS: int = 60

    width: int = 1920
    height: int = 1080
    helper: Utility = Utility()
    background = helper.getColor("BROWN")
    screen: pygame.Surface
    running: bool
    flags: int
    truck: Vehicle
    mine: Storage
    homebase: Storage
    gasstation: Storage
    helicopter: Vehicle
    spriteGroup: pygame.sprite.Group
    clock = pygame.time.Clock()
    truckGasInfo: Text
    truckStorageInfo: Text
    hudelements: typing.List[Text]
    hudimages: typing.List[pygame.Surface]
    ai: VehicleAi
    winAmount: int

    def __init__(self: App):
        pygame.init()
        self.flags = RESIZABLE
        self.screen = pygame.display.set_mode((self.width, self.height), self.flags)
        pygame.display.set_caption("|".join((self.TITLE, self.VERSION)))
        self.running = True

        self.createSprites()
        self.winAmount = self.mine.getMaxAmount() * 80 / 100

    def createSprites(self : App):
        self.truck = Vehicle(30, 0.1, 9, False, 150)
        self.helicopter = Vehicle(30, 0.6,  15, True, 50)
        self.ai = VehicleAi(self.helicopter)
        image = pygame.image.load("data/images/mine.png")
        self.mine = Storage(self.MINESTORAGE, self.MINESTORAGE, image)
        self.mine.rect = self.mine.rect.move(5,5)
        image = pygame.image.load("data/images/home.png")
        self.homebase = Storage(self.MINESTORAGE, image = image)
        self.homebase.rect = self.homebase.rect.move(1500, 730)
        image = pygame.image.load("data/images/gasstation.png")
        self.gasstation = Storage(0, image = image)
        self.gasstation.rect = self.gasstation.rect.move(1300, 10)

        self.spriteGroup = pygame.sprite.Group()
        self.spriteGroup.add(self.truck, self.mine, self.homebase, self.gasstation, self.helicopter)

        self.truckStorageInfo = Text('', pos=(1650, 1020))
        self.truckGasInfo = Text('', pos=(1800, 1020))
        self.hudelements = [self.truckGasInfo, self.truckStorageInfo]

        coalimg = pygame.image.load("data/images/coalhud.png")
        coalpos = (1608,1020)
        gasimage = pygame.image.load("data/images/gashud.png")
        gaspos = (1776,1020)
        self.hudimages = [(coalimg, coalpos), (gasimage, gaspos)]


    def run(self: App):
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                # print(event)
                if event.type == QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[K_a]:
                self.truck.turnLeft()
            if keys[K_d]:
                self.truck.turnRight()
            if keys[K_s]:
                self.truck.brake()
            elif keys[K_w]:
                self.truck.accelerate()
            else:
                self.truck.decelerate()
            if keys[K_f]:
                self.attemptFill(self.truck, self.mine)
            if keys[K_e]:
                self.attemptEmpty(self.truck, self.homebase)
            if keys[K_q]:
                self.attemptFillGas(self.truck, self.gasstation)

            print(self.ai.decideAction(self.truck))

            if self.checkWinCondition():
                self.screen.fill(self.helper.getColor("GREEN"))
                Text('Congratulations! You win!', (800,540)).draw(self.screen)
                pygame.display.update()
            elif self.checkLoseCondition():
                self.screen.fill(self.helper.getColor("RED"))
                Text('Game over! Try again', (800,540)).draw(self.screen)
                pygame.display.update()
            else:
                self.spriteGroup.update()
                self.updateInfos()
                self.drawStuff()

        pygame.quit()

    def drawStuff(self: App):
        self.screen.fill(self.background)
        self.spriteGroup.draw(self.screen)
        for element in self.hudelements:
            element.draw(self.screen)
        for (image,pos) in self.hudimages:
            self.screen.blit(image, pos)
        pygame.display.update()

    def updateInfos(self: App):
        truckGas = "{} l".format(self.truck.getGas().__round__())
        self.truckGasInfo.setText(truckGas)
        truckStorage = "{} / {} t".format(self.truck.getStorage().getAmount(), self.truck.getStorage().getMaxAmount())
        self.truckStorageInfo.setText(truckStorage)

    def toggle_fullscreen(self):
        """Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)

    def attemptFill(self: App, toFill: Vehicle, toEmpty: Storage):
        if((toFill.getSpeed() > 0) or not self.helper.proximity(toFill.getRect(), toEmpty.getRect())):
            return False
        else:
            fillAmount = toFill.getStorage().getMaxAmount() - toFill.getStorage().getAmount()
            toFill.getStorage().fill(toEmpty.empty(fillAmount))
            return True

    def attemptEmpty(self: App, toEmpty: Vehicle, toFill: Storage):
        if((toEmpty.getSpeed() > 0) or not self.helper.proximity(toFill.getRect(), toEmpty.getRect())):
            return False
        else:
            emptyAmount = toEmpty.getStorage().getAmount()
            toFill.fill(toEmpty.getStorage().empty(emptyAmount))
            return True

    def attemptFillGas(self: App, toFill: Vehicle, gasstation: Storage):
        if(toFill.getSpeed() > 0 or not self.helper.proximity(toFill.getRect(), gasstation.getRect())):
            return False
        else:
            toFill.setGas(toFill.getMaxGas())
            return True
        
    def checkWinCondition(self: App) -> bool:
        if(self.homebase.getAmount() >= self.winAmount):
            return True
        else:
            return False

    def checkLoseCondition(self: App) -> bool:
        if ((self.mine.getAmount() + self.homebase.getAmount()) < self.winAmount) or (self.truck.getGas() <= 0 and not self.checkWinCondition()):
            return True
        else:
            return False


if __name__ == '__main__':
    App().run()