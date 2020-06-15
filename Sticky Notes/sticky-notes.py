import PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QPlainTextEdit, QPushButton,QGridLayout, QWidget
import sys


class StickyNotes(QMainWindow):
	def __init__(self):
		super().__init__()
		self.PATH = 'C:\\Users\\Shubh\\Desktop\\projects\\Automate Notes\\notes.txt'
		self.initUI()

	def initUI(self):
		fonts = QtGui.QFont('Helvetica', 10)
		resolution = QDesktopWidget().screenGeometry()
		grid = QGridLayout()

		self.template = QWidget(self)
		self.setCentralWidget(self.template)

		self.setGeometry(resolution.width() - 195, 265, 175, 200)
		self.setWindowTitle('NOTES')
		self.setWindowIcon(QtGui.QIcon('note.png'))

		self.save = QPushButton()
		self.save.setIcon(QtGui.QIcon('save.png'))
		self.save.setIconSize(QtCore.QSize(15, 15))
		self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.save.setToolTip('save')
		self.save.setStyleSheet('padding: 0px; background-color: transparent; margin: 0px')
		self.save.clicked.connect(self.saveNotes)
		grid.addWidget(self.save, 0, 0)

		self.textArea = QPlainTextEdit()
		self.textArea.setFont(fonts)
		self.textArea.setStyleSheet('margin: 0px')
		grid.addWidget(self.textArea, 1, 0, 1, 10)
		
		self.template.setLayout(grid)
		self.openNotes()
		self.show()

	def openNotes(self):
		with open(self.PATH, 'r') as f:
			self.textArea.insertPlainText(f.read())

	def saveNotes(self):
		with open(self.PATH, 'w') as f:
			f.write(self.textArea.toPlainText())


if __name__ == '__main__':
	note = QApplication(sys.argv)
	window = StickyNotes()
	sys.exit(note.exec_())

