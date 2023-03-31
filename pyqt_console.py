#!/usr/bin/python3

"""
Inspired by:
    ZetCode PyQt5 tutorial
    Author: Jan Bodnar
    Website: zetcode.com

Setup: on macos
brew install qt
pip install PyQt6  # Use version 6 as version 5 wouln't install on macos
"""

import sys
import subprocess
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication,  QPlainTextEdit, QLineEdit
from PyQt6.QtGui import QTextCursor, QFont
from PyQt6 import QtCore


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        buttons = []
        btn1 = QPushButton("date", self)
        btn1.move(30, 30)
        buttons.append(btn1)

        btn2 = QPushButton("hostname", self)
        btn2.move(145, 30)
        buttons.append(btn2)

        btn3 = QPushButton("whoami", self)
        btn3.move(260, 30)
        buttons.append(btn3)

        btn4 = QPushButton("custom command", self)
        btn4.move(375, 30)
        btn4.resize(150, 30)
        buttons.append(btn4)

        btn5 = QPushButton("exit", self)
        btn5.move(730, 30)
        buttons.append(btn5)

        for btn in buttons:
            btn.clicked.connect(self.buttonClicked)

        font_textbox = QFont('Consolas', 12)
        font_console = QFont('Consolas', 10)

        self.textbox = QLineEdit(self)
        self.textbox.move(540, 30)
        self.textbox.resize(180,30)
        self.textbox.setFont(font_console)

        self.statusBar()

        self.textArea = QPlainTextEdit(self)
        self.textArea.move(10, 75)
        self.textArea.resize(880, 550)  #x,y
        self.textArea.setFont(font_console)

        cursor = QTextCursor(self.textArea.document())
        cursor.setPosition(0)
        self.textArea.setTextCursor(cursor)

        self.setGeometry(300, 300, 920, 700)
        self.setWindowTitle('Quick console')
        self.show()

    def quit(self):
        QtCore.QCoreApplication.instance().quit()


    def buttonClicked(self):

        sender = self.sender()
        command = sender.text().lower()
        self.statusBar().showMessage(command + ' was pressed')

        textboxValue = self.textbox.text()

        if command == 'exit':
            self.quit()
            return
        if command == "custom command":
            if textboxValue:
                command = textboxValue
            else:
                command = "echo"  # hack that does nothing really

        ps = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = ps.communicate()
        lines = stdout.decode().splitlines()
        errcode = ps.returncode

        self.statusBar().showMessage(f'retcode: {errcode}')
        self.textArea.insertPlainText(f"\nCommand: {command}\n")

        for line in lines:
            self.textArea.insertPlainText(f"{line}\n")

        self.textArea.ensureCursorVisible()



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
