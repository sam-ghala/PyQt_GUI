from PyQt5.QtCore import QDate, QTime, QDateTime, Qt #importing files
#print current date
now = QDate.currentDate()
#print(now)
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print(" ")

dateTime = QDateTime.currentDateTime()
print(dateTime.toString())

time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))

# number of days in a month and year
d = QDate(1945, 5, 7)
print("Days in month: %s" % d.daysInMonth())
print("Days in year: %s" % d.daysInYear())
# days passed since christmas
xmas2 = QDate(2018, 12, 24)
now = QDate.currentDate()
daysPassed = xmas2.daysTo(now)
print("%s days have passed since last Christmas." % daysPassed)
print(" ")
# time and dates adding and subtracting
now = QDateTime.currentDateTime()
print("Today: %s"% now.toString(Qt.ISODate))
print("Adding 12 days: %s" % now.addDays(12).toString(Qt.ISODate))
print("Subtracting 22 days: %s" % now.addDays(-22).toString(Qt.ISODate))
print("Adding 55 seconds: %s"%now.addSecs(55).toString(Qt.ISODate))
print("Adding 3 months: %s" % now.addMonths(3).toString(Qt.ISODate))
print("Adding 12 years: %s" % now.addYears(12).toString(Qt.ISODate))
print(" ")
# daylight time
from PyQt5.QtCore import QTimeZone
now = QDateTime.currentDateTime()
print("Time zone: %s" % now.timeZoneAbbreviation())
if now.isDaylightTime():
    print('The current date falls into DST time')
else:
    print("The current date does not fall into DST time")

#%% GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(350,150)
w.move(300,300)
w.setWindowTitle('Simple First')
w.show()
sys.exit(app.exec_())
# icon in window
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
#%% push button
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(100,100)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('ToolTips')
        self.show()
        
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec())
#%% Closing a window
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        self.setGeometry(300,300,450,150)
        self.setWindowTitle('Quit Button')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())        
#%% message box
import sys
from PyQt5.QtWidgets import (QWidget, QMessageBox, QApplication)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
