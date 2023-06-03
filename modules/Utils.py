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
        """creates a new Utility"""
        return

    def getColor(self : Utility, color: str) -> typing.List[int]:
        """Returns a rgb triplet if a valid color is given.
        False otherwise
        """
        if(color in self.COLORS):
            return self.COLORS[color]
        else:
            return False

    def rotateCenter(self: Utility, image: pygame.Surface, topLeft: pygame.Tuple[int, int], angle: float):
        """Helperfunction to turn pygame image and rectangle around its center.
        Returns a Tuple containing the rotated image and rectangle.
        """
        rotated_image = pygame.transform.rotate(image, angle)
        rect = rotated_image.get_rect(center = image.get_rect(topleft = topLeft).center)
        return [rotated_image, rect]

    def proximity(self: Utility, rect1: pygame.Rect, rect2: pygame.Rect, inflate: int = 20) -> bool: 
        """Returns True if the both rectangles are in a given distance of each other."""
        rect1Inflated = rect1.inflate(inflate, inflate)
        rect2Inflated = rect2.inflate(inflate, inflate)
        return rect2Inflated.colliderect(rect1Inflated)
    
    def distance(self: Utility, pointa: typing.Tuple[int,int], pointb: typing.Tuple[int,int]) -> float:
        """Returns the distance between to given points."""
        return ((pointb[0] - pointa[0])**2 + (pointb[1] - pointa[1])**2)**0.5