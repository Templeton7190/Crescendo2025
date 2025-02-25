from typing import Final


class ControllerConstants:
    PORT: Final = 0


class DriveConstants:
    REAR_LEFT_MOTOR_CHANNEL: Final = 1
    FRONT_LEFT_MOTOR_CHANNEL: Final = 2
    FRONT_RIGHT_MOTOR_CHANNEL: Final = 3
    REAR_RIGHT_MOTOR_CHANNEL: Final = 4

    DRIVING_MOTOR_FACTOR: Final = 0.5
    SIDEWAYS_MOTOR_FACTOR: Final = 0.5
    TURNING_MOTOR_FACTOR: Final = 0.5


class GrabberConstants:
    MOTOR_CHANNEL: Final = 5
    MOTOR_SPEED: Final = 0.25
    HOLD_SPEED: Final = 0.05


class ElevatorConstants:
    LEFT_MOTOR_CHANNEL: Final = 6
    RIGHT_MOTOR_CHANNEL: Final = 7

    MOTOR_SPEED: Final = 0.5
    DROP_SPEED: Final = -1.0


class AlgaeConstants:
    MOTOR_CHANNEL: Final = 8

    MOTOR_SPEED: Final = 0.5


class ClimberConstants:
    MOTOR_CHANNEL: Final = 9

    MOTOR_SPEED: Final = 1.0
