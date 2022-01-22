import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import main

class App(QWidget):
    print('in class')
    def __init__(self, count=None, str=None):
        global hotButton, coldButton, LightButton, distressButton, TVButton, channel1Button, channel2Button, channel3Button

        print('in init')
        self.str = str
        self.count = count
        print(self.count)
        if self.count == 0:
            print('in init 2')
            super().__init__()
            self.title = 'Smart Home'
            self.left = 750
            self.top = 450
            self.width = 750
            self.height = 480
            hotButton = QPushButton('heat', self)
            # buttonHOT.setToolTip('this is an example button')
            hotButton.move(80, 150)
            # buttonHOT.clicked.connect(self.on_click)
            hotButton.setStyleSheet("background-color : red")
            coldButton = QPushButton('cold', self)
            # buttonHOT.setToolTip('this is an example button')
            coldButton.move(200, 150)
            # buttonHOT.clicked.connect(self.on_click)
            coldButton.setStyleSheet("background-color : red")
            LightButton = QPushButton('light', self)
            # buttonHOT.setToolTip('this is an example button')
            LightButton.move(500, 150)
            # buttonHOT.clicked.connect(self.on_click)
            LightButton.setStyleSheet("background-color : red")
            # self.initUI()

            distressButton = QPushButton('distress button', self)
            # buttonHOT.setToolTip('this is an example button')
            distressButton.move(500, 300)
            # buttonHOT.clicked.connect(self.on_click)
            distressButton.setStyleSheet("background-color : red")
            TVButton = QPushButton('TV', self)
            # buttonHOT.setToolTip('this is an example button')
            TVButton.move(150, 250)
            # buttonHOT.clicked.connect(self.on_click)
            TVButton.setStyleSheet("background-color : red")
            channel1Button = QPushButton('channel 1', self)
            # buttonHOT.setToolTip('this is an example button')
            channel1Button.move(10, 300)
            # buttonHOT.clicked.connect(self.on_click)
            channel1Button.setStyleSheet("background-color : red")
            channel2Button = QPushButton('channel 2', self)
            # buttonHOT.setToolTip('this is an example button')
            channel2Button.move(150, 300)
            # buttonHOT.clicked.connect(self.on_click)
            channel2Button.setStyleSheet("background-color : red")
            channel3Button = QPushButton('channel 3', self)
            # buttonHOT.setToolTip('this is an example button')
            channel3Button.move(290, 300)
            # buttonHOT.clicked.connect(self.on_click)
            channel3Button.setStyleSheet("background-color : red")

            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.show()

        else:
            if self.str == "cold":
                self.move(coldButton)
            elif self.str == "heat":
                self.move(hotButton)
            elif self.str == "help":
                self.move(distressButton)
            elif self.str == "tv":
                self.move(TVButton)
            elif self.str == "channel one":
                self.move(channel1Button)
            elif self.str == "channel two":
                self.move(channel2Button)
            elif self.str == "channel three":
                self.move(channel3Button)
            elif self.str =="light off":
                LightButton.setStyleSheet("background-color : red")
            elif self.str == "light on":
                self.move(LightButton)
            elif self.str == "no help":
                distressButton.setStyleSheet("background-color : red")
            print("change color")

    def move(self, model):
        print("change color of button")
        model.setStyleSheet("background-color : green")

    #



