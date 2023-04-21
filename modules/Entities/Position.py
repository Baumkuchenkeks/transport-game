from __future__ import annotations

class Position:
    x: int
    y: int

    def getX(self: Position) -> int :
        return self.x
    
    def setX(self: Position, newX: int) -> Position:
        self.x = newX
        return self
    
    def getY(self: Position) -> int:
        return self.y
    
    def setY(self: Position, newY: int) -> Position:
        self.y = newY
        return self