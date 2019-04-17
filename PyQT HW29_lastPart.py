#
#
#

from PyQt5 import QtCore, QtGui, QtWigets
#
import rPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmde(GPIO.BCM)
led = LED(23)
led_pin=24
GPIO.setup(led_pin,GPIO.OUT)
pwm = GPIO.PWM(led_pin,100)
pwm.start(100)
def ledToggle():
    if led.is_lit:
        led.off()
    else:
        led.on()
class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        mainWindow.reseize(615,310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget. setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QCore.QRect(70,50,171,151))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectname("pushButton")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        #
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        #
        self.verticalSlider.setGeomerty(QtCore.QRect(410,50,22,160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setOvjectName("verticalSlider")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380,220,101,22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidgets(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusbar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","MainWindow"))
        self.pushButton.setText(_translate("MainWindow","Toggle LED"))
        self.lineEdit.setText(_translate("MainWindow","LED Brightness"))
        
        self.pushButton.clicked.conect(ledToggle)
        self.verticalSlider.valueChanged.connect(self.sliderMov)
    def sliderMov(self):
        value = self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
import sys
app = QtWidgets.QApplication(sys.agv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
  