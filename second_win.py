class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set.appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    
    def initUI(self):
        self.name = QLabel(txt_name)
        self.hintname = QLineEdit(txt_hintname)
        self.hintage = QLabel(txt_hintage)
        self.age = QLineEdit(txt_age)
        self.test1 = QLabel(txt_test1)
        self.btn1 = QPushButton(txt_starttest1)
        self.restest1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.btn2 = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.btn3 = QPushButton(txt_starttest3)
        self.restest2 = QLineEdit(txt_hinttest2)
        self.restest3 = QLineEdit(txt_hinttest3)
        self.btn4 = QPushButton(txt_sendresults)

        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        
        self.l_line.addWidget(self.name)
        self.l_line.addWidget(self.hintname)
        self.l_line.addWidget(self.hintage)
        self.l_line.addWidget(self.age)
        self.l_line.addWidget(self.test1)
        self.l_line.addWidget(self.btn1)
        self.l_line.addWidget(self.restest1)
        self.l_line.addWidget(self.test2)
        self.l_line.addWidget(self.btn2)
        self.l_line.addWidget(self.test3)
        self.l_line.addWidget(self.btn3)
        self.l_line.addWidget(self.restest2)
        self.l_line.addWidget(self.restest3)
        self.l_line.addWidget(self.btn4, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.timer)
        self.h_line.addWidget(self.r_line)
        self.h_line.addWidget(self.h_line)
        
        self.setLayout(self.h_line)


    def connects(self):
        self.btn_next.clicke

    def next_click(self):
        self.hide()
        final_win.set_appear()

tw = TestWin()
