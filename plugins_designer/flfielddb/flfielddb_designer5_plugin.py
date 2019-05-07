# -*- coding: utf-8 -*-

#Based on https://github.com/pyqt/examples/blob/master/designer/plugins/python/analogclockplugin.py

from PyQt5.Qt import QIcon,QPixmap
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin

from flfielddb import FLFieldDB

import os

class FLFieldDBPluging(QPyDesignerCustomWidgetPlugin):
    
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
        return FLFieldDB(parent)
    
    def name(self):
        return "FLFieldDB"
    
    def group(self):
        return "Pineboo"

    def icon(self):
        return QIcon(QPixmap(os.path.realpath(os.path.join(os.path.dirname(__file__), "./icons/dataline.png"))))
    
    def toolTip(self):
        return "FLFieldDB Widget"
    
    def whatsThis(self):
        return "A widget for data base fields"

    def isContainer(self):
        return False
    
    def includeFile(self):
        return "flfielddb"
    
    
    