# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


import os


class PNCore(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    @QtCore.pyqtSlot()
    def execDefaultScript(self):
        pass

    @QtCore.pyqtSlot()
    def openDefaultForm(self):
        pass
