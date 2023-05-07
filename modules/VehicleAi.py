from __future__ import annotations
from .Entities.Vehicle import Vehicle
from .Utils import Utility
import typing

class VehicleAi:
    MODE_HUNT = "hunt"
    MODE_HOME = "home"
    TURN_LEFT = "Ai turned left"
    TURN_RIGHT = "Ai turned right"
    ACCELERATE = "Ai sped up"
    BRAKE = "Ai slowed down"
    STORAGE = "Ai stole stuff"

    vehicle : Vehicle
    mode: str

    def __init__(self: VehicleAi, vehicle: Vehicle) -> None:
        self.vehicle = vehicle
        self.mode = VehicleAi.MODE_HUNT

    def decideAction(self: VehicleAi, enemy: Vehicle) -> str:
        enemyPosition = enemy.getRect().center
        enemySpeed = enemy.getSpeed()
        enemydirection = enemy.getDirection()
        aimove = ""
        helper = Utility()
        if self.mode == VehicleAi.MODE_HUNT:
            horizontalvertical = "{}{}".format(self.enemyHorizontal(enemyPosition[0]), self.enemyVertical(enemyPosition[1]))
            if horizontalvertical == "00":
                if(self.vehicle.direction == enemydirection):
                    ##direction is correct -> match speed
                    if(enemySpeed > self.vehicle.speed):
                        self.vehicle.accelerate()
                        aimove += VehicleAi.ACCELERATE
                    elif(enemySpeed < self.vehicle.speed):
                        self.vehicle.brake()
                        aimove += VehicleAi.BRAKE
                else:
                    aimove += self.decideTurn(enemydirection)
            else:
                directiongoal = self.decideDirection(horizontalvertical)
                if self.vehicle.direction == directiongoal:
                    ##decide if enemy is far enough away to accelerate TODO
                    self.vehicle.accelerate()
                    aimove += VehicleAi.ACCELERATE
                else:
                    aimove += self.decideTurn(directiongoal)
            if helper.proximity(self.vehicle.getRect(), enemy.getRect()):
                ""
        return aimove
        
    def enemyHorizontal(self: VehicleAi, enemyx) -> int:
        if(self.vehicle.rect.centerx < enemyx):
            return 1
        if(self.vehicle.rect.centerx > enemyx):
            return -1
        return 0
    
    def enemyVertical(self: VehicleAi, enemyy :int) -> int:
        if(self.vehicle.rect.centery < enemyy):
            return 1
        if(self.vehicle.rect.centery > enemyy):
            return -1
        return 0
    
    def decideTurn(self: VehicleAi, directiongoal: int) -> str:
                ##### DECIDE HOW TO TURN #####
        maxrotation = abs(directiongoal - self.vehicle.direction)
        if self.vehicle.direction < directiongoal:
            if (self.vehicle.direction + 180) < directiongoal:
                self.vehicle.turnRight(maxrotation)
                return VehicleAi.TURN_LEFT
            else:
                self.vehicle.turnLeft(maxrotation)
                return VehicleAi.TURN_RIGHT
        else:
            if (self.vehicle.direction - 180) > directiongoal:
                self.vehicle.turnLeft(maxrotation)
                return VehicleAi.TURN_RIGHT
            else:
                self.vehicle.turnRight(maxrotation)
                return VehicleAi.TURN_LEFT

    def decideDirection(self: VehicleAi, matchcode: str) -> int:
        match matchcode:
            case "01": ## enemyposition is directly down 90°
                directiongoal = 90
            case "10": ## enemyposition is directly right 175°
                directiongoal = 175
            case "11": ## enemyposition is downright 135°
                directiongoal = 135
            case "0-1":## enemyposition is directly up 275°
                directiongoal = 275
            case "1-1":## enemyposition is upright 45°
                directiongoal = 225
            case "-10":## enemyposition is directly left 0°
                directiongoal = 0
            case "-11":## enemyposition is downleft 45°
                directiongoal = 45
            case "-1-1":## enemyposition is upfleft 315°
                directiongoal = 315
        return directiongoal