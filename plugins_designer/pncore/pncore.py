# -*- coding: utf-8 -*-
from PyQt6 import QtCore, QtWidgets


class PNCore(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    @QtCore.pyqtSlot()
    def execDefaultScript(self):
        pass

    @QtCore.pyqtSlot()
    def openDefaultForm(self):
        pass
