import commands2 as c2
import wpilib

from constants import ElevatorConstants


class Elevator(c2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor = wpilib.PWMSparkMax(ElevatorConstants.LEFT_MOTOR_CHANNEL)

    def up(self) -> None:
        self.motor.set(ElevatorConstants.MOTOR_SPEED)

    def down(self) -> None:
        self.motor.set(-ElevatorConstants.MOTOR_SPEED)

    def drop(self) -> None:
        self.motor.set(ElevatorConstants.DROP_SPEED)

    def stop(self) -> None:
        self.motor.set(0)
