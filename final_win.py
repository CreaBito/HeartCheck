from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from instr import *


class FinalWin(QWidget):
    def __init__(self) :
        super().__init__()
        self.set_appear()
  
        self.initUI()
  
        self.show()
    def initUI(self):

      self.final_index = QLabel(txt_index)
      self.final_result = QLabel(txt_workheart)

      self.layout_line = QVBoxLayout()

      self.layout_line.addWidget(self.final_index, alignment = Qt.AlignCenter)
      self.layout_line.addWidget(self.final_result, alignment = Qt.AlignCenter)
      self.setLayout(self.layout_line)

    def set_appear(self):
      self.setWindowTitle(txt_finalwin)
      self.resize(win_w,win_h)
      
