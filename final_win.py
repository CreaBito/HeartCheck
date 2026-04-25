from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from instr import *


class MainWin(QWidget):
    def __init__(self) :
        super().__init__()
        self.set_appear()
  
        self.initUI()
  
        self.show()
    def initUI(self):
      self.text_hi = QLabel(txt_index)
      self.text_instruction = QLabel(txt_workheart)

      self.layout_line = QVBoxLayout()

      self.layout_line.addWidget(self.text_hi, alignment = Qt.AlignLeft)
      self.layout_line.addWidget(self.txt_instruction, alignment = Qt.AlignLeft)
      self.setLayout(self.layout_line)

    def set_appear(self):
      self.setWindowTitle(txt_title)
      self.resize(win_w,win_h)
