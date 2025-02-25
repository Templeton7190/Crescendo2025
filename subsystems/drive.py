import commands2 as c2
import phoenix5
import wpilib.drive
from constants import DriveConstants


class Drive(c2.Subsystem):
    def __init__(self) -> None:
        super().__init__()

        frontLeftMotor = phoenix5.WPI_TalonSRX(DriveConstants.FRONT_LEFT_MOTOR_CHANNEL)
        rearLeftMotor = phoenix5.WPI_TalonSRX(DriveConstants.REAR_LEFT_MOTOR_CHANNEL)

        frontRightMotor = phoenix5.WPI_TalonSRX(
            DriveConstants.FRONT_RIGHT_MOTOR_CHANNEL
        )
        rearRightMotor = phoenix5.WPI_TalonSRX(DriveConstants.REAR_RIGHT_MOTOR_CHANNEL)

        self.drive = wpilib.drive.MecanumDrive(
            frontLeftMotor, rearLeftMotor, frontRightMotor, rearRightMotor
        )

    def driveCartesian(self, xSpeed: float, ySpeed: float, zRotation: float) -> None:
        self.drive.driveCartesian(
            xSpeed,
            ySpeed,
            zRotation,
        )
