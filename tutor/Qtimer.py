# from PyQt5.QtCore import *
# def timeout():
#     print("this is time-out")

# def init():
#     timer = QTimer()
#     timer.setInterval(1000)
#     timer.timeout.connect(timeout)
#     timer.start()

# init()

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)

interval=1000
time=0
timerVar = QTimer()

def setinterval():
    timerVar.setInterval(interval)

def printTime():
    global time, interval
    time +=1
    if time%10==0:
        interval=2000
        setinterval()
    print(QTime.currentTime())

# timerVar.setInterval(interval)
timerVar.timeout.connect(printTime)
timerVar.start(interval)

app.exec_()
