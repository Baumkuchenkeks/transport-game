from __future__ import annotations

import pygame

class Utility:
    COLORS = {
        "GREEN": (150, 255, 150),
        "RED": (255, 0, 0),
        "YELLOW": (255, 255, 0),
        "CYAN": (0, 255, 255),
        "MAGENTA": (255, 0, 255),
        "BLACK": (0, 0, 0),
        "GRAY": (100, 100, 100)
    }

    def __init__(self : Utility):
        return

    def getColor(self : Utility, color: str):
        if(color in self.COLORS):
            return self.COLORS[color]
        else:
            return False

    def rotateCenter(self: Utility, image: pygame.Surface, topLeft: pygame.Tuple[int, int], angle: float):
        rotated_image = pygame.transform.rotate(image, angle)
        rect = rotated_image.get_rect(center = image.get_rect(topleft = topLeft).center)
        return [rotated_image, rect]
        # screen.blit(rotated_image, rect.topleft)