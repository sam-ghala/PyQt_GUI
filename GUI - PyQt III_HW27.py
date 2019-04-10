#
# Sam Ghalayini 
# CE 232 Python Programming - PyQt GUI 3 - HW 27
# 4/09/2019
#

# Absolute Positioning
import sys 
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lbl1 = QLabel('Zeetcode',self)
        lbl1.move(15,10)
        lbl2 = QLabel('tutorials',self)
        lbl2.move(35,40)
        lbl3 = QLabel('for porgramers',self)
        lbl3.move(55,70)
        self.setGeometry(300,300,450,150)
        self.setWindowTitle('Absolute')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Box Layout
import sys 
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttttons')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Grid Layout
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls','Bck',',','Close','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            gird.addWidget(button,*position)
        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Reivew Example
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGridLayout, QTextEdit, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)
        
        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)
        self.setLayout(grid)
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Review')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Event and Signal
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300,300,350,150)
        self.setWindowTitle('Signal and slot')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Reimplementing event handler
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,450,150)
        self.setWindowTitle('Event handler')
        self.show()
    def keyPressEvent(self,s):
        if s.key() == Qt.Key_Escape:
            self.close()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Even Object
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget ,QLabel, QGridLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        x = 0
        y = 0
        self.test = "x: {0}, y: {1}".format(x,y)
        self.label = QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)
        self.setmouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(300,300,450,200)
        self.setWindowTitle('Event Object')
        self.show()
    def mouseMoveEvent(self,e):
        x = e.x()
        y = e.y()
        text = "x: {0}, y: {1}".format(x,y)
        self.label.setText(text)

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Event Sender
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow ,QPushButton, QApplication)

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30,50)
        
        btn2 = QPushButton("Button 2",self)
        btn2.move(150,50)
        
        btn1.clicked.connect(self.buttonCLicked)
        btn2.clicked.connect(self.buttonCLicked)
        self.statusBar()
        self.setGeometry(300,300,450,200)
        self.setWindowTitle('Event Sender')
        self.show()
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " was pressed")
    
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Emit signals
import sys
from PyQt5.QtCore import pyqtSignal, QObject 
from PyQt5.QtWidgets import (QMainWindow , QApplication)

class Communicate(QObject):
    closeApp = pyqtSignal()
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setGeometry(300,300,290,150)
        self.setWindowTItle('Emit signal')
        self.show()
        
    def mousePressEvent(self,event):
        self.c.closeApp.emit()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Dialogs
import sys
from PyQt5.QtWidgets import(QWidget, QPushButton, QLineEdit, QInputDialog , QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.btn = QPushButton("Dialog",self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        self.le = QLineEdit(self)
        self.le.move(130,22)
        self.setGeometry(300,300,390,150)
        self.setWindowTitle('dialog')
        self.show()
    def showDialog(self):
        text,ok = QInputDialog.getText(self,'Dialog','Enter your name:')
        if ok:
            self.le.setText(str(text))

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
    
# Color Dialog
import sys
from PyQt5.QtWidgets import(QWidget, QPushButton, QFrame, QColorDialog , QApplication)
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        col = QColor(0,0,0)
        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget ( background-color: %s )" % col.name())
        self.frm.setGeometry(130,22,100,100)
        self.setGeometry(300,300,350,180)
        self.setWindowTitle('Color Dialog')
        self.show()
    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget ( background-color: %s )" % col.name())

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# Font Dialog
import sys
from PyQt5.QtWidgets import(QWidget, QPushButton, QVBoxLayout, QSizePolicy, QLabel, QFontDialog , QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        vbox = QVBoxLayout()
        btn = QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(20,20)
        vbox.addWidget(btn)
        btn.clicked.connect(self.showDialog)
        self.lbl = QLabel("Knowledge only matters",self)
        self.lbl.move(130,20)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        self.setGeometry(300,300,350,180)
        self.setWindowTitle('Font Dialog')
        self.show()
    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
            
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

# File Dialog
import sys
from PyQt5.QtWidgets import(QWidget, QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWdiget(self.textEdit)
        self.statusBar()
        openFile = QAction(QIcon('open.png'),'Open',self)
        openFile .setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        self.setGeomerty(300,300,350,300)
        self.setWindowTitle('File Dialog')
        self.show()
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'Open File','/home')
        if fname[0]:
            f = open(fname[0],'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
                
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())    
        




















