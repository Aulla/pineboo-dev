# -*- coding: utf-8 -*-

# Based on https://github.com/pyqt/examples/blob/master/designer/plugins/python/analogclockplugin.py

from PyQt6 import QtGui, QtDesigner

import pncore

import os


class PNCoreDBPluging(QtDesigner.QPyDesignerCustomWidgetPlugin):
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
        return pncore.PNCore(parent)

    def name(self):
        return "PNCore"

    def group(self):
        return "Pineboo"

    def icon(self):
        return QtGui.QIcon(
            QtGui.QPixmap(
                os.path.realpath(os.path.join(
                    os.path.dirname(__file__), "../icons/dataline.png"))
            )
        )

    def toolTip(self):
        return "PNCore Widget"

    def whatsThis(self):
        return "A widget for data base fields"

    def isContainer(self):
        return False

    def includeFile(self):
        return "pncore"
