from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self) :
        super().__init__()
        self.set_appear()
  
        self.initUI()
  
        self.connects()
  
        self.show()
    def initUI(self):
      self.text_hi = QLabel(txt_hi)
      self.text_instruction = QLabel(txt_instruction)
      self.btn_next = QPushButton(tx_next, self)

      self.layout_line = QVBoxLayout()

      self.layout_line.addWidget(self.text_hi, alignment = Qt.AlignLeft)
      self.layout_line.addWidget(self.text_instruction, alignment = Qt.AlignLeft)
      self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
      self.setLayout(self.layout_line)
    
    def click_pushnext(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.click_pushnext)


    def set_appear(self):
      self.setWindowTitle(txt_title)
      self.resize(win_w,win_h)
      


app = QApplication([])
mw = MainWin()
app.exec_()
