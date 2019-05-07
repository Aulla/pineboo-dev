# -*- coding: utf-8 -*-

#Based on https://github.com/pyqt/examples/blob/master/designer/plugins/python/analogclockplugin.py

from PyQt5.Qt import QIcon,QPixmap
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.Qt import QIcon,QPixmap

from fltabledb import FLTableDB

import os

class FLTableDBPluging(QPyDesignerCustomWidgetPlugin):
    
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
        return FLTableDB(parent)
    
    def name(self):
        return "FLTableDB"
    
    def group(self):
        return "Pineboo"

    def icon(self):
        return QIcon(QPixmap(os.path.realpath(os.path.join(os.path.dirname(__file__), "./icons/datatabledb.png"))))
    
    def toolTip(self):
        return "FLTableDB Widget"
    
    def whatsThis(self):
        return "A widget for data base tables"

    def isContainer(self):
        return False
    
    def includeFile(self):
        return "fltabledb"

    