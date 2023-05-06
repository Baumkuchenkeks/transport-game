from __future__ import annotations

import pygame
import typing

class Utility:
    COLORS = {
        "GREEN": (150, 255, 150),
        "RED": (255, 0, 0),
        "YELLOW": (255, 255, 0),
        "CYAN": (0, 255, 255),
        "MAGENTA": (255, 0, 255),
        "BLACK": (0, 0, 0),
        "GRAY": (100, 100, 100),
        "BROWN": (111, 73, 29)
    }

    def __init__(self : Utility):
        return

    def getColor(self : Utility, color: str) -> typing.List[int]:
        if(color in self.COLORS):
            return self.COLORS[color]
        else:
            return False

    def rotateCenter(self: Utility, image: pygame.Surface, topLeft: pygame.Tuple[int, int], angle: float):
        rotated_image = pygame.transform.rotate(image, angle)
        rect = rotated_image.get_rect(center = image.get_rect(topleft = topLeft).center)
        return [rotated_image, rect]

    def proximity(self: Utility, rect1: pygame.Rect, rect2: pygame.Rect):
        rect1Inflated = rect1.inflate(20, 20)
        rect2Inflated = rect2.inflate(20, 20)
        return rect2Inflated.colliderect(rect1Inflated)