from typing import Final
import rev


BRUSHED: Final = rev.SparkLowLevel.MotorType.kBrushed
BRUSHLESS: Final = rev.SparkLowLevel.MotorType.kBrushless


class ControllerConstants:
    PORT: Final = 0


class DriveConstants:
    REAR_LEFT_MOTOR_CHANNEL: Final = 1
    FRONT_LEFT_MOTOR_CHANNEL: Final = 2
    FRONT_RIGHT_MOTOR_CHANNEL: Final = 3
    REAR_RIGHT_MOTOR_CHANNEL: Final = 4

    DRIVING_MOTOR_FACTOR: Final = 1.0
    SIDEWAYS_MOTOR_FACTOR: Final = 0.5
    TURNING_MOTOR_FACTOR: Final = 0.5


class AlgaeConstants:
    MOTOR_CHANNEL: Final = 9

    MOTOR_SPEED: Final = 0.25


class ClimberConstants:
    MOTOR_CHANNEL: Final = 7

    MOTOR_SPEED: Final = 0.25


class ElevatorConstants:
    MOTOR_CHANNEL: Final = 0

    MOTOR_SPEED: Final = 0.5
    DROP_SPEED: Final = -1.0


class GrabberConstants:
    MOTOR_CHANNEL: Final = 5

    MOTOR_SPEED: Final = 0.4
    HOLD_SPEED: Final = 0.2
