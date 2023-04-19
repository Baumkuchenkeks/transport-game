from __future__ import annotations

class Constants:
    COLORS = {
        "GREEN": (150, 255, 150),
        "RED": (255, 0, 0),
        "YELLOW": (255, 255, 0),
        "CYAN": (0, 255, 255),
        "MAGENTA": (255, 0, 255),
        "BLACK": (0, 0, 0),
        "GRAY": (100, 100, 100)
    }

    def __init__(self : Constants):
        return

    def getColor(self, color: str):
        if(color in self.COLORS):
            return self.COLORS[color]
        else:
            return False
