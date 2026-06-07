import os
import time

import commands2
# import phoenix5
import wpilib

from addressableLEDs import addressableLEDs


class WestCoastRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        super().__init__()

        self.addressableLEDs = addressableLEDs()
        self.pongController = wpilib.XboxController(0)

        # self.gridlength = 16
        # self.gridwidth = 16
        self.gridlength = 10
        self.gridwidth = 18

        self.addressableLEDs.lightPongStart(gridlength=self.gridlength, gridwidth=self.gridwidth)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.lightPong(True, True)


    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        self.addressableLEDs.lightPongStart(gridlength=self.gridlength, gridwidth=self.gridwidth)

        time.sleep(1)


    def teleopPeriodic(self):
        # self.addressableLEDs.lightLEDs(wpilib.Color.kAzure)
        # self.addressableLEDs.lightMatrix(gridwidth = 18, gridlength = 10, LEDPattern=[
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        # ])
        # self.addressableLEDs.lightExtendedMatrix(gridwidth = 18, gridlength = 10, LEDPattern=[
        # #   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                                                                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        # ])
        self.lightPong(False, False)

    def testInit(self):
        pass

    def testPeriodic(self):
        pass

    def lightPong(self, leftauto, rightauto):
        leftauto = leftauto
        rightauto = rightauto
        if self.addressableLEDs.lightPongPeriodic(self.pongController.getLeftY(), self.pongController.getRightY(), leftauto, rightauto) is not None:
            if self.addressableLEDs.lightPongPeriodic(self.pongController.getLeftY(), self.pongController.getRightY(), leftauto, rightauto) == "left":
                self.addressableLEDs.rightscore += 1
            elif self.addressableLEDs.lightPongPeriodic(self.pongController.getLeftY(), self.pongController.getRightY(), leftauto, rightauto) == "right":
                self.addressableLEDs.leftscore += 1
            time.sleep(0.5)
            self.addressableLEDs.lightLEDs(wpilib.Color.kBlack)
            time.sleep(1.0)
            self.addressableLEDs.lightPongStart(gridlength=self.gridlength, gridwidth=self.gridwidth)
        if self.addressableLEDs.leftscore >= 10 or self.addressableLEDs.rightscore >= 10:
            print("Game Over!")
            self.addressableLEDs.lightLEDs(wpilib.Color.kAzure)
            time.sleep(10)
            self.addressableLEDs.lightLEDs(wpilib.Color.kBlack)
            os._exit(1)
            
if __name__ == "__main__":
    wpilib.run(WestCoastRobot)
