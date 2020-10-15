#!/usr/bin/env python

#  Copyright (c) 2020. CJ Associates

import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from ui_johndemo import Ui_JohnDemo


class JohnDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_JohnDemo()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionWombat.triggered.connect(self.update_status)
        self.ui.actionOpen.triggered.connect(self.select_file)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open the dang file', os.getcwd())
        self.ui.statusbar.showMessage(f'You chose {file_path}', 0)

    def update_status(self):
        self.ui.statusbar.showMessage('ANIMAL!', 3000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = JohnDemoMain()
    main.show()
    sys.exit(app.exec_())
