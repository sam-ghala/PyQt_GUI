#
#
#

# ardunio serical. collect serial datausing ardunio, windows, 
import serial 
import matplotlib.pyplot as plt
ser = serial.Serial('COM3',9600)
n = 0
dataLst = []
while n<200: # collect 200 data points
    print(ser.readline())
    dataPoint = ser.readline()
    dataPoint = int(dataPoint) # data recivied are strings
    dataLst.append(dataPoint)
    n+=1
#print(type(dataPoint))
#print(dataPoint)
ser.close()

plt.plot(dataLst) # plot data
plt.show() # dont need htis if i run it in spyder
f = open("sericalData.dat","w") # save data to a file
f.write(str(dataLst)) # string only when writing into a file
f.close()
f = open("sericalData.dat","r")
print(f.read())
### using pyplot to plot data instead of matplotlib
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import PlotWidget
import numpy as np

x = np.array([1,2,3])
y = np.array([1,2,3])
pg.setConfigOption('background','w')
penn = pg.mkPen('k',width = 2, style = QtCore.Qt.SolidLine)
p1 = pg.plot(x,y,pen = penn, title='The First pyqtgraph Plot',symbol = 't', symbolSize = 20)
p1.setXRange(0,4)
p1.setYRange(0,4)
p1.setlabel('left','Voltage','V')
p1.setlabel('bottom','Time','s')
QtGui.QApplication.exec_()
### plot in GUI
from pyQt5 import QtGui, QtCore
import pyqtgraph as pg

app = QtGui.QApplication([])
w = QtGui.QWidget()
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('enter text')
listw = QtGui.QListWidget()
pg.setConfigOptoin('background','w')
plt = pg.PlotWidget()
penn = pg.mkPen('k',width = 2, style = QtCore.Qt.SolidLine)
plt.plot([1,2,3],[1,2,3],pen=penn,title = 'The first pyqtgraph plot',symbol = 't', symbolSize = 20)
labelStyle = {'color':'#000','font-size':'30px'}
plt.setLabel('bottom','Time','s',**labelStyle)
plt.setLabel('left','Voltage','V',**labelStyle)
plt.setYRange(0,5)
plt.setXRange(0,5)
layout = QtGui.QGridLayout()
w.setLayout(layout)
layout.addWidget(btn,0,0)
layout.addWidget(text,1,0)
layout.addWidget(listw,2,0)
layout.addWidget(plt,0,1,3,1)
w.show()
app.exec_()
#####
import spidev
from numpy import interp
from time import sleep
##
from PyQt5 import QtCore,QtGui,QtWidgets
from pyqtgraph import plotWidget
import serial
from PyQt5 import QtGui,QtCore
import sys
import numpy as np
import pyqtgraph

#ser = serial.Serial('COM3',9600)
##
spi = spidev.SpiDev()
spi.open(0,0)
##
class ExampleApp(QtGui.QMainWindow):
    def __inint__(self):
        super().__init__()
        pyqtgraph.setConfigOption('background','w')
        self.setupUi(self)
        
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350,300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20,20,300,300))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
    ##
    def analogInput(self,channel):
        spi.max_speed_hz = 1350000
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3)<<8) + adc[2]
        return data
    ##
    def update(self):
        points = 100
        X = np.arange(points)
        n = 0
        dataLst = []
        while n < 100:
            dataPoint = self.analogInput(0) # reading from Ch0
            dataLst.append(dataPoint)
            n+=1
        Y = dataLst
        penn = pyqtgraph.mkPen('k',width = 3, style = QtCore.Qt.SolidLine)
        self.graphicsView.setYRange(0,1200,padding = 0)
        labelStyle = {'color':'#000','font-size':'20px'}
        self.graphicsView.setLabel('bottom','Number of Points','',**labelStyle)
        self.graphicsView.setlabel('left','Voltage','',**labelStyle)
        self.graphicsView.plot(X,Y,pen = penn, clear = True)
        QtCore.QTimer.singleShot(1,self.update)

app = QtGui.QApplication(sys.argv)
form = ExampleApp()
form.show()
form.update()
app.exec_()
####
import spidev
from numpy import interp
from time import sleep

spi = spidev.SpiDev()
spi.open()

def analogInput(self,channel):
    spi.max_speed_hz = 1350000
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3)<<8) + adc[2]
    return data
while True:
    output = analogInput(0) #reading from ch0
    print(output)
    sleep(0.1)





























