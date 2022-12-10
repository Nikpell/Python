import sys

from PyQt5 import QtWidgets

import ui_MyForm

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = ui_MyForm.Ui_MainWindow()
ui.setupUi(window)
ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)
window.show()
sys.exit(app.exec_())
