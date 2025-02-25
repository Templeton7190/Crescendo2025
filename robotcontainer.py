import commands2 as c2
from constants import ControllerConstants, DriveConstants
import subsystems


class RobotContainer:
    def __init__(self) -> None:
        self.drive = subsystems.Drive()
        self.grabber = subsystems.Grabber()
        self.elevator = subsystems.Elevator()
        self.algae = subsystems.Algae()
        self.climber = subsystems.Climber()

        self.controller = c2.button.CommandXboxController(ControllerConstants.PORT)

        self.configureButtonBindings()

        self.drive.setDefaultCommand(
            c2.RunCommand(
                lambda: self.drive.driveCartesian(
                    self.controller.getLeftX() * DriveConstants.DRIVING_MOTOR_FACTOR,
                    self.controller.getLeftY() * DriveConstants.SIDEWAYS_MOTOR_FACTOR,
                    self.controller.getRightX() * DriveConstants.TURNING_MOTOR_FACTOR,
                ),
                self.drive,
            )
        )

    def getAutonomousCommand(self) -> c2.Command | None:
        return

    def configureButtonBindings(self) -> None:
        # grabber
        self.controller.b().whileTrue(
            c2.cmd.runEnd(self.grabber.up, self.grabber.stop, self.grabber)
        )
        self.controller.a().whileTrue(
            c2.cmd.runEnd(self.grabber.down, self.grabber.stop, self.grabber)
        )
        # elevator
        self.controller.povUp().whileTrue(
            c2.cmd.runEnd(self.elevator.up, self.elevator.stop, self.elevator)
        )
        self.controller.povDown().whileTrue(
            c2.cmd.runEnd(self.elevator.drop, self.elevator.stop, self.elevator)
        )
        # climber
        self.controller.leftTrigger().whileTrue(
            c2.cmd.runEnd(self.climber.up, self.climber.stop, self.climber)
        )
        self.controller.leftBumper().whileTrue(
            c2.cmd.runEnd(self.climber.down, self.climber.stop, self.climber)
        )
        # algae
        self.controller.rightTrigger().whileTrue(
            c2.cmd.runEnd(self.algae.clockwise, self.algae.stop, self.algae)
        )
        self.controller.rightBumper().whileTrue(
            c2.cmd.runEnd(self.algae.counterClockwise, self.algae.stop, self.algae)
        )
