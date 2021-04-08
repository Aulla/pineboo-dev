# -*- coding: utf-8 -*-

# Based on https://github.com/pyqt/examples/blob/master/designer/plugins/python/analogclockplugin.py
import os
import fltable

from PyQt6 import QtDesigner, QtGui


class FLTableluging(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initialized = False

    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return fltable.FLTable(parent)

    def name(self):
        return "FLTable"

    def group(self):
        return "Pineboo"

    def icon(self):
        return QtGui.QIcon(QtGui.QPixmap(os.path.realpath(os.path.join(os.path.dirname(__file__), "./icons/designer_table.png"))))

    def toolTip(self):
        return "FLTable Widget"

    def whatsThis(self):
        return "A widget for data"

    def isContainer(self):
        return False

    def includeFile(self):
        return "fltable"
