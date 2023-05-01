from __future__ import annotations
import pygame
from pygame.locals import *
from modules.Utils import Utility
from modules.Entities.Vehicle import Vehicle
from modules.Entities.Storage import Storage

class App:
    TITLE = "transport-game"
    VERSION = "0.01-07042023"

    MINESTORAGE = 3000
    FPS: int = 60

    width: int = 1920
    height: int = 1080
    constantHelper: Utility = Utility()
    background = constantHelper.getColor("BROWN")
    screen: pygame.Surface
    running: bool
    flags: int
    truck: Vehicle
    mine: Storage
    homebase: Storage
    # helicopter: Vehicle = Vehicle(30, 0.6,  15, True, 50, [5, 5])
    spriteGroup: pygame.sprite.Group
    clock = pygame.time.Clock()

    def __init__(self: App):
        pygame.init()
        self.flags = RESIZABLE
        self.screen = pygame.display.set_mode((self.width, self.height), self.flags)
        pygame.display.set_caption("|".join((self.TITLE, self.VERSION)))
        self.running = True

        self.createSprites()

    def createSprites(self : App):
        self.truck = Vehicle(30, 0.1, 9, False, 150)
        image = pygame.image.load("data/images/mine.png")
        self.mine = Storage(self.MINESTORAGE, self.MINESTORAGE, image)
        self.mine.rect = self.mine.rect.move(5,5)
        image = pygame.image.load("data/images/home.png")
        self.homebase = Storage(self.MINESTORAGE, image = image)
        self.homebase.rect = self.homebase.rect.move(1500,730)

        self.spriteGroup = pygame.sprite.Group()
        self.spriteGroup.add(self.truck, self.mine, self.homebase)

    def run(self: App):
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                print(event)
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
                
            # self.helicopter.moveTowards(self.truck, self)
            self.spriteGroup.update()
            self.screen.fill(self.background)
            self.spriteGroup.draw(self.screen)
            pygame.display.update()
        pygame.quit()
    
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

if __name__ == '__main__':
    App().run()