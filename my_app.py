from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQtS.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, Label, GListWidget, QLineEdit)




from instr.py import*
from second_win.py import*
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()# устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы
        self.connects() # устанавливает связи между элементами
        self.show() # старт


    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self): 
        self.hello_text = QLabel( txt_hello )
        self.instruction = QLabel( txt_instruction )
        self.button = QPushButton( txt_next )
        self.layout = QVBoxLayout()
        self.hello_text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addWidget(self.layout)

    def connects(self): 
        self.bnt_next.clicked.connect( self.next_click )
        
    def next_click(self):
        self.hide()
        self.tw = TestWin()
        
app = QAplication([])
mw = MainWin()
app.exec_()
