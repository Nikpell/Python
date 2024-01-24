from PyQt5 import QtWidgets, QtGui, QtCore
from qlabel import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __int__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setFont(QtGui.QFont('SansSerif', 30))

        self.setGeometry(QtCore.QRect(10, 10, 200, 200))


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
