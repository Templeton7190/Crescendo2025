import commands2 as c2
import wpilib
import subsystems


class Autonomous(c2.Command):
    def __init__(self, grabber: subsystems.Grabber) -> None:
        super().__init__()
        self.grabber = grabber
        self.timer = wpilib.Timer()
        self.addRequirements(grabber)

    def initialize(self) -> None:
        self.timer.reset()

    def execute(self) -> None:
        self.grabber.up()

    def end(self, interrupted: bool) -> None:
        self.grabber.stop()
        self.timer.stop()

    def isFinished(self) -> bool:
        return self.timer.get() > 2.5
