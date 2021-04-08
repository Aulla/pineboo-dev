# -*- coding: utf-8 -*-

# Based on https://github.com/pyqt/examples/blob/master/designer/plugins/python/analogclockplugin.py

from PyQt6 import QtGui, QtDesigner

import fltabledb
import os


class FLTableDBPluging(QtDesigner.QPyDesignerCustomWidgetPlugin):

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
        return fltabledb.FLTableDB(parent)

    def name(self):
        return "FLTableDB"

    def group(self):
        return "Pineboo"

    def icon(self):
        return QtGui.QIcon(QtGui.QPixmap(os.path.realpath(os.path.join(os.path.dirname(__file__), "./icons/datatabledb.png"))))

    def toolTip(self):
        return "FLTableDB Widget"

    def whatsThis(self):
        return "A widget for data base tables"

    def isContainer(self):
        return False

    def includeFile(self):
        return "fltabledb"
