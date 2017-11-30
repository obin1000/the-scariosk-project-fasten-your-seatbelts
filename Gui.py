import sys
#import time
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		print('Scariosk wordt opgestart')
		print('Live feed wordt laten zien')
		self.b = QtWidgets.QPushButton('Take photo')
		self.b1 = QtWidgets.QPushButton('New photo')
		self.b1.hide()
		self.l = QtWidgets.QLabel('Live feed')

		h_box = QtWidgets.QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.l)
		h_box.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.b)
		v_box.addWidget(self.b1)
		v_box.addLayout(h_box)

		self.setLayout(v_box)
		self.setWindowTitle('Scariosk photobooth')
		self.setGeometry(150, 100, 350, 450)

		self.b.clicked.connect(self.btn_click)
		self.b1.clicked.connect(self.btn_click1)

		self.show()

	def btn_click(self):
		print('Foto wordt gemaakt')
		self.l.setPixmap(QtGui.QPixmap('Test.png'))
		self.b.hide()
		self.b1.show()

	def btn_click1(self):
		print('Live feed wordt laten zien')
		self.l.setText('Take new photo')
		self.b1.hide()
		self.b.show()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
