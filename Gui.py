import sys
import time
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
		self.l1 = QtWidgets.QLabel('Foto wordt gemaakt in')
		self.l1.hide()
		self.l2 = QtWidgets.QLabel('5')
		self.l2.hide()
		self.l3 = QtWidgets.QLabel('4')
		self.l3.hide()
		self.l4 = QtWidgets.QLabel('3')
		self.l4.hide()

		h_box = QtWidgets.QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.l)
		h_box.addWidget(self.l1)
		h_box.addWidget(self.l2)
		h_box.addWidget(self.l3)
		h_box.addWidget(self.l4)
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
		self.l.hide()
		self.l1.show()
		time.sleep(1)
		print('5')
		self.l1.hide()
		self.l2.show()
		time.sleep(1)
		print('4')
		self.l2.hide()
		self.l3.show()
		time.sleep(1)
		print('3')
		self.l3.hide()
		self.l4.show()
		time.sleep(1)
		self.l4.hide()
		self.l.show()
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
