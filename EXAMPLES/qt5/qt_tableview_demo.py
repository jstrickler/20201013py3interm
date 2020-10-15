#!/usr/bin/env python
import sys

from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class FilterDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_elements()

    def init_elements(self):
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.reject)

        okButton = QPushButton("OK")
        okButton.setDefault(True)
        okButton.clicked.connect(self.accept)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)
        hbox.addWidget(okButton)

        self.regex = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.regex)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Filter Column')


class FilterModel(QSortFilterProxyModel):
    def __init__(self, filters):
        super().__init__()
        self.filters = filters

    def filterAcceptsRow(self, row, modelindex):
        for i, filter in enumerate(self.filters):
            if filter not in str(self.sourceModel().index(row, i).data()):
                return False
        return True


class WordListViewer(QMainWindow):
    def __init__(self, path):
        super().__init__()
        self.dbpath = path
        self.init_elements()

    def init_elements(self):
        exitAct = QAction(QIcon.fromTheme('exit'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.statusBar().showMessage(self.dbpath)

        self.init_table()

        self.setCentralWidget(self.table)

        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('FormTable viewer')

        self.show()

    def init_table(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.dbpath)
        if not db.open():
            raise Error("Could not open the database")

        self.model = QSqlTableModel(self, db)
        self.model.setTable("presidents")
        self.model.EditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.table = QTableView()
        self.table.setSortingEnabled(True)
        self.add_filter_functionality()
        self.table.show()

    def add_filter_functionality(self):
        def show_filter(logical_index):
            dialog = FilterDialog(self)
            if not dialog.exec_():
                return
            filter = dialog.regex.text()
            self.filters.filters[logical_index] = filter
            print(self.filters.filters)
            self.filters.modelReset.emit()

        self.filters = FilterModel([""] * self.model.columnCount())
        self.filters.setSourceModel(self.model)
        self.table.setModel(self.filters)
        self.filters.modelReset.emit()

        header = self.table.horizontalHeader()
        header.sectionDoubleClicked.connect(show_filter)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = WordListViewer('../../DATA/presidents.db')

    sys.exit(app.exec_())
