from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        t1 = int(self.exp.test1)
        t2 = int(self.exp.test2)
        t3 = int(self.exp.test3)
        self.index = (4 * (t1 + t2 + t3) - 200) / 10
        self.set_appear()
        self.initUI()
        self.show()

    def initUI(self):
        self.final_index = QLabel(txt_index + str(self.index))
        self.final_result = QLabel(txt_workheart + self.results())
        layout = QVBoxLayout()
        layout.addWidget(self.final_index, alignment=Qt.AlignCenter)
        layout.addWidget(self.final_result, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_w, win_h)

    def results(self):
            age = int(self.exp.person.age)
            index = self.index
            if age >= 15:
                if index >= 15:
                    return txt_res1
                elif index >= 11:
                    return txt_res2
                elif index >= 6:
                    return txt_res3
                elif index >= 0.5:
                    return txt_res4
                else:
                    return txt_res5
            elif age == 13 or age == 14:
                if index >= 16.5:
                    return txt_res1
                elif index >= 12.5 or index <= 16.5:
                    return txt_res2
                elif index >= 7.5 or index <= 12.4:
                    return txt_res3
                elif index >= 2 or index <= 7.4:
                    return txt_res4
                else:
                    return txt_res5
            elif age == 11 or age == 12:
                if index >= 18:
                    return txt_res1
                elif index >= 14 or index <= 17.9:
                    return txt_res2
                elif index >= 9 or index <= 13.9:
                    return txt_res3
                elif index >= 3.5 or index <= 8.9:
                    return txt_res4
                else:
                    return txt_res5
            elif age == 9 or age == 10:
                if index >= 19.5:
                    return txt_res1
                elif index >= 15.5 or index <= 19.4:
                    return txt_res2
                elif index >= 10.5 or index <= 15.4:
                    return txt_res3
                elif index >= 5 or index <= 10.4:
                    return txt_res4
                else:
                    return txt_res5
            elif age == 7 or age == 8:
                if index >= 21:
                    return txt_res1
                elif index >= 17 or index <= 20.9:
                    return txt_res2
                elif index >= 12 or index <= 16.9:
                    return txt_res3
                elif index >= 6.5 or index <= 11.9:
                    return txt_res4
                else:
                    return txt_res5
