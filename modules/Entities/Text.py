from __future__ import annotations

import pygame
import typing
from ..Utils import Utility

class Text:
    """Create a text object."""
    text: str
    fontname: str
    fontsize: int
    fontcolor: typing.List[int]
    img: pygame.Surface
    rect: pygame.rect.Rect

    def __init__(self: Text, text: str, pos, **options):
        """creates a new Text"""
        helper: Utility = Utility()
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 42
        self.fontcolor = helper.getColor('BLACK')
        self.set_font()
        self.render()

    def set_font(self: Text):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self: Text):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self: Text, screen: pygame.Surface):
        """Draws the Text onto a given surface"""
        screen.blit(self.img, self.rect)
    
    def setText(self: Text, text: str):
        self.text = text
        self.render()