import commands2 as c2
import rev
from constants import BRUSHED, GrabberConstants


class Grabber(c2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        self.motor = rev.SparkMax(GrabberConstants.MOTOR_CHANNEL, BRUSHED)
        self.motor.setInverted(True)

    def up(self) -> None:
        self.motor.set(GrabberConstants.MOTOR_SPEED)

    def down(self) -> None:
        self.motor.set(-GrabberConstants.MOTOR_SPEED)

    def hold(self) -> None:
        self.motor.set(GrabberConstants.HOLD_SPEED)

    def stop(self) -> None:
        """Sets the motor speed to 0"""
        self.motor.set(0)

    def set(self, speed: float) -> None:
        """Sets the motor speed between -1.0 and 1.0"""
        self.motor.set(speed)
