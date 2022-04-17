
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.line = QVBoxLayout()
        result = (4*(restest1+restest2+restest3)-200)/10
        self.layout.addWidget(self.txt_index + str(result))
        if 7 <= age <= 8:
            if result >= 21:
                heart = 'Низкая'
            elif 17 <= result <= 20,9:
                heart = 'Удовлетворительная'
            elif 12 <= result <= 16,9:
                heart = 'Средняя'
            elif 6,5 <= result <= 11,9:
                heart = 'Выше среднего'
            else:
                heart = 'Высокий'
        
        elif 9 <= age <= 10:
            if result >= 19,5:
                heart = 'Низкая'
            elif 15,5 <= result <= 19,4:
                heart = 'Удовлетворительная'
            elif 10,5 <= result <= 15,4:
                heart = 'Средняя'
            elif 5 <= result <= 10,4:
                heart = 'Выше среднего'
            else:
                heart = 'Высокий'
        
        elif 13 <= age <= 14:
            if result >= 16,5:
                heart = 'Низкая'
            elif 12,5 <= result <= 16,4:
                heart = 'Удовлетворительная'
            elif 7,5 <= result <= 12,4:
                heart = 'Средняя'
            elif 2 <= result <= 7,4:
                heart = 'Выше среднего'
            else:
                heart = 'Высокий'
        
        elif age >= 15:
            if result >= 15:
                heart = 'Низкая'
            elif 11 <= result <= 14,9:
                heart = 'Удовлетворительная'
            elif 6 <= result <= 10,9:
                heart = 'Средняя'
            elif 0,5 <= result <= 5,9:
                heart = 'Выше среднего'
            else:
                heart = 'Высокий'
        
        self.layout.addWidget(self.txt_workheart + heart)
