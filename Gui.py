import sys
import time
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		print('Scariosk wordt opgestart...')
		print('Live feed wordt laten zien')
		self.button1 = QtWidgets.QPushButton('Take photo')
		self.button2 = QtWidgets.QPushButton('New photo')
		self.button2.hide()
		self.label1 = QtWidgets.QLabel('Live feed')
		self.label2 = QtWidgets.QLabel('Foto wordt gemaakt in')
		self.label2.hide()
		self.label3 = QtWidgets.QLabel('5')
		self.label3.hide()
		self.label4 = QtWidgets.QLabel('4')
		self.label4.hide()
		self.label5 = QtWidgets.QLabel('3')
		self.label5.hide()

		h_box = QtWidgets.QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.label1)
		h_box.addWidget(self.label2)
		h_box.addWidget(self.label3)
		h_box.addWidget(self.label4)
		h_box.addWidget(self.label5)
		h_box.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.button1)
		v_box.addWidget(self.button2)
		v_box.addLayout(h_box)

		self.setLayout(v_box)
		self.setWindowTitle('Scariosk photobooth')
		self.setGeometry(150, 100, 350, 450)

		self.button1.clicked.connect(self.btn_click)
		self.button2.clicked.connect(self.btn_click1)

		self.show()

	def btn_click(self):
		print('Foto wordt gemaakt')
		self.label1.hide()
		self.label2.show()

		time.sleep(1)
		print('5')
		self.label2.hide()
		self.label3.show()

		time.sleep(1)
		print('4')
		self.label3.hide()
		self.label4.show()

		time.sleep(1)
		print('3')
		self.label4.hide()
		self.label5.show()

		time.sleep(1)
		self.label5.hide()
		self.label1.show()
		self.label1.setText('Test.png')
		self.button1.hide()
		self.button2.show()

	def btn_click1(self):
		print('Live feed wordt laten zien')
		self.label1.setText('Take new photo')
		self.button2.hide()
		self.button1.show()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
