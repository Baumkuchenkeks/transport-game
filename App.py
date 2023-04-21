from __future__ import annotations
import pygame
from pygame.locals import *
from modules.Constants import Constants
from modules.Entities.Vehicle import Vehicle

class App:
    TITLE = "transport-game"
    VERSION = "0.01-07042023"

    width: int = 1920
    height: int = 1080
    constantHelper: Constants = Constants()
    background = constantHelper.getColor("BLACK")
    screen: pygame.Surface
    running: bool
    flags: int
    truck: Vehicle = Vehicle(30, 5, 90, False, 150)
    helicopter: Vehicle = Vehicle(30, 10,  150, True, 50, [5, 5])
    spriteGroup: pygame.sprite.Group

    def __init__(self: App):
        pygame.init()
        self.flags = RESIZABLE
        self.screen =App.screen = pygame.display.set_mode((self.width, self.height), self.flags)
        pygame.display.set_caption("|".join((self.TITLE, self.VERSION)))
        self.running = True
        self.spriteGroup = pygame.sprite.Group()
        self.spriteGroup.add(self.truck, self.helicopter)
        

    def run(self: App):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    match event.key:
                        case pygame.K_F12:
                            self.toggle_fullscreen()
                        case pygame.K_w:
                            self.truck.accelerate()
                        case pygame.K_a:
                            self.truck.turnLeft()
                        case pygame.K_s:
                            self.truck.decelerate()
                        case pygame.K_d:
                            self.truck.turnRight()
                        case _:
                            None
            self.helicopter.moveTowards(self.truck, self)
            self.spriteGroup.update()
            App.screen.fill(App.background)
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





# screen = pygame.display.set_mode((width, height)) #Surface object
# pygame.display.set_caption("|".join((TITLE, VERSION)))

# ball = pygame.image.load("data/images/ball.gif")
# rect = ball.get_rect()
# speed = [2, 2]

# while True:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == QUIT:
#             pygame.quit()
#         if event.type == KEYDOWN:
#             match event.key:
#                 case pygame.K_w:
#                     background = constantHelper.getColor("CYAN")
#                 case pygame.K_a:
#                     background = constantHelper.getColor("YELLOW")
#                 case pygame.K_s:
#                     background = constantHelper.getColor("MAGENTA")
#                 case pygame.K_d:
#                     background = constantHelper.getColor("BLACK")
#                 case _:
#                     None
#     rect = rect.move(speed)
#     if rect.left < 0 or rect.right > width:
#         speed[0] = -speed[0]
#     if rect.top < 0 or rect.bottom > height:
#         speed[1] = -speed[1]
#     screen.fill(background)
#     pygame.draw.rect(screen, constantHelper.getColor("RED"), rect, 1)
#     screen.blit(ball, rect)
#     pygame.display.update()