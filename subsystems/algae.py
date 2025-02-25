import commands2 as c2
import wpilib

from constants import AlgaeConstants


class Algae(c2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor = wpilib.PWMSparkMax(AlgaeConstants.MOTOR_CHANNEL)

    def clockwise(self) -> None:
        self.motor.set(AlgaeConstants.MOTOR_SPEED)

    def counterClockwise(self) -> None:
        self.motor.set(-AlgaeConstants.MOTOR_SPEED)

    def stop(self) -> None:
        self.motor.set(0)
