import commands2 as c2
import phoenix5
import wpilib.drive
from constants import DriveConstants
from wpimath.filter import SlewRateLimiter


class Drive(c2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        frontLeftMotor = phoenix5.WPI_VictorSPX(DriveConstants.FRONT_LEFT_MOTOR_CHANNEL)
        rearLeftMotor = phoenix5.WPI_VictorSPX(DriveConstants.REAR_LEFT_MOTOR_CHANNEL)

        frontRightMotor = phoenix5.WPI_VictorSPX(
            DriveConstants.FRONT_RIGHT_MOTOR_CHANNEL
        )
        rearRightMotor = phoenix5.WPI_VictorSPX(DriveConstants.REAR_RIGHT_MOTOR_CHANNEL)

        self.drive = wpilib.drive.MecanumDrive(
            frontLeftMotor, rearLeftMotor, frontRightMotor, rearRightMotor
        )
        self.forwardFilter = SlewRateLimiter(1)

    def driveCartesian(self, xSpeed: float, ySpeed: float, zRotation: float) -> None:
        self.drive.driveCartesian(
            zRotation * DriveConstants.TURNING_MOTOR_FACTOR,
            xSpeed * DriveConstants.SIDEWAYS_MOTOR_FACTOR,
            self.forwardFilter.calculate(-ySpeed) * DriveConstants.DRIVING_MOTOR_FACTOR,
        )
