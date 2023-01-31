from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from menu import Ui_inicial


if __name__== "__main__":
      app = QtWidgets.QApplication(sys.argv)
      window = QtWidgets.QWidget()
      ui = Ui_inicial()
      ui.setupUi(window)
      window.show()
      sys.exit(app.exec_())
