import sys

from PyQt6 import uic, QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    ServerAdress = "https://localhost:5000/"
    MessageId = 0

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('messanger.ui', self)
        # self.pushButton.clicked.connect(self.pushButton_clicked)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
