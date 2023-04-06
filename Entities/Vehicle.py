from __future__ import annotations

import pygame
import Position
import Storage


class Vehicle(pygame.sprite.Sprite):
    weight: float
    position: Position
    maxSpeed: float
    isFlying: bool
    storage: Storage

    def move(direction : str) -> bool :
        return True
