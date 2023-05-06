from __future__ import annotations
from .Entities.Vehicle import Vehicle
import typing

class VehicleAi:
    MODE_HUNT = "hunt"
    MODE_HOME = "home"

    vehicle : Vehicle
    mode: str

    def __init__(self: VehicleAi, vehicle: Vehicle) -> None:
        self.vehicle = vehicle
        self.mode = VehicleAi.MODE_HUNT

    def decideAction(self: VehicleAi, enemyPosition: typing.Tuple[int,int], enemySpeed: float, enemydirection: int) -> function:
        if self.mode == VehicleAi.MODE_HUNT:
            horizontalvertical = "{}{}".format(self.enemyHorizontal(enemyPosition[0]), self.enemyVertical(enemyPosition[1]))
            match horizontalvertical:
                case "00": ## position is correct
                    if(self.vehicle.direction == enemydirection):
                        if(enemySpeed > self.vehicle.speed):
                            self.vehicle.accelerate()
                        elif(enemySpeed < self.vehicle.speed):
                            self.vehicle.brake()
                    else:
                        ##### DECIDE HOW TO TURN #####
                        ""
                case "01":
                    ""
                case "10":
                    ""
                case "11":
                    ""
                case "0-1":
                    ""
                case "1-1":
                    "
                case "-10":
                    ""
                case "-11":
                    ""
                case "-1-1":
                    ""
            return 
        
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