from robotcontainer import RobotContainer
import commands2 as c2


class MyRobot(c2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.autonomousCommand: c2.Command | None = None
        self.container = RobotContainer()

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.getAutonomousCommand()

        if self.autonomousCommand is not None:
            self.autonomousCommand.schedule()
        else:
            print("No autonomous command")

    def teleopInit(self) -> None:
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    def testInit(self) -> None:
        c2.CommandScheduler.getInstance().cancelAll()
