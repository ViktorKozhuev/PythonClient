import json
import sys
import datetime

import requests
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from requests import HTTPError


class MainWindow(QtWidgets.QMainWindow):
    ServerAdress = "http://127.0.0.1:5000"
    MessageId = 0

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('messanger.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        self.SendMessage()

    def SendMessage(self):
        UserName = self.lineEdit.text()
        MessageText = self.lineEdit_2.text()
        TimeStamp = str(datetime.datetime.today())
        msg = f"{{\"UserName\": \"{UserName}\", \"MessageText\":\"{MessageText}\", \"TimeStamp\":\"{TimeStamp}\"}}"
        print("Отправлено сообщение: ", msg)
        url = self.ServerAdress + "/api/Messanger"
        data = json.loads(msg)
        r = requests.post(url, json=data)
        print(r.status_code, r.reason)

    def GetMessage(self, id):
        url = self.ServerAdress + "/api/Messanger/" + str(id)
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print()
            return None
        else:
            text = response.text
            return text

    def timerEvent(self):
        msg = self.GetMessage(self.MessageId)
        while msg is not None:
            msg = json.loads(msg)
            UserName = msg['UserName']
            MessageText = msg['MessageText']
            TimeStamp = msg['TimeStamp']
            msgtext = f"{TimeStamp} : <{UserName}> : <{MessageText}>"
            print(msgtext)
            self.listWidget_1.insertItem(self.MessageId, msgtext)
            self.MessageId += 1
            msg = self.GetMessage(self.MessageId)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    timer = QtCore.QTimer()
    time = QtCore.QTime(0, 0, 0)
    timer.timeout.connect(w.timerEvent)
    timer.start(5000)
    sys.exit(app.exec())
