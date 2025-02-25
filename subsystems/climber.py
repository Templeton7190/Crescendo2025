import commands2 as c2
import wpilib

from constants import ClimberConstants


class Climber(c2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor = wpilib.PWMSparkMax(ClimberConstants.MOTOR_CHANNEL)

    def up(self) -> None:
        self.motor.set(ClimberConstants.MOTOR_SPEED)

    def down(self) -> None:
        self.motor.set(-ClimberConstants.MOTOR_SPEED)

    def stop(self) -> None:
        self.motor.set(0)
