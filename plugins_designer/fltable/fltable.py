# -*- coding: utf-8 -*-

from PyQt5.Qt import QIcon,QPixmap, QTextFormat, QTextEdit
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton,\
    QTableView, QVBoxLayout
from PyQt5.QtCore import pyqtProperty, Q_ENUMS
from PyQt5 import QtCore

from enum import Enum
import os



class SelectionModeEnum(Enum):
    Single, Multi, SingleRow, MultiRow, NoSelection = range(5)

class FocusStyleEnum(Enum):
    FollowStyle, SpreadSheet = range(2) 
    
class FLTable(QWidget):
    
    table_view = None
    _num_rows = None
    _num_cols = None
    _show_grid = False
    _row_moving_enabled = False
    _column_moving_enabled = False
    _read_only = None
    _sorting = None
    _selection_mode = None
    _focus_style = None
    _default_row_height = None
    _default_col_width = None
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.table_view = QTableView(self)
        
        lay = QVBoxLayout()
        lay.addWidget(self.table_view)
        
        self.setLayout(lay)
        
        self._num_rows = 0
        self._num_cols = 0
        self._show_grid = True
        self._row_moving_enabled = False
        self._column_moving_enabled = False
        self._read_only = False
        self._sorting = False
        self._selection_mode = 1
        self._focus_style = 1
        
        self._default_col_width = 100
        self._default_row_height = 20
        
        
    Q_ENUMS(SelectionModeEnum)
    Q_ENUMS(FocusStyleEnum)
    
    def setNumRows(self, nr):
        self._num_rows = nr
    
    def setNumCols(self, nc):
        self._num_cols = nc
    
    def setShowGrid(self, sg):
        self._show_grid = sg
    
    def setRowMovingEnabled(self, me):
        self._row_moving_enabled = me
    
    def setColumnMovingEnabled(self, me):
        self._column_moving_enabled = me
    
    def setReadOnly(self, ro):
        self._read_only = ro
    
    def setSorting(self, s):
        self._sorting = s
    
    def setSelectionMode(self, sm):
        self._selection_mode = sm
    
    def setFocusStyle(self, fe):
        self._focus_style = fe
    
    def setDefaultRowHeight(self, re):
        self._default_row_height = re
    
    def setDefaultColumnWidth(self, cw):
        self._default_col_width = cw
    
    def get_num_rows(self):
        return self._num_rows
    
    def get_num_cols(self):
        return self._num_cols
    
    def get_show_grid(self):
        return self._show_grid
    
    def get_row_moving_enabled(self):
        return self._row_moving_enabled
    
    def get_column_moving_enabled(self):
        return self._column_moving_enabled
    
    def get_read_only(self):
        return self._read_only
    
    def get_sorting(self):
        return self._sorting
    
    def get_selection_mode(self):
        return self._selection_mode
    
    def get_focus_style(self):
        return self._focus_style
    
    def get_default_row_height(self):
        return self._default_row_height
    
    def get_default_column_width(self):
        return self._default_col_width
    
    
    numRows = pyqtProperty(int, get_num_rows, setNumRows)
    numCols = pyqtProperty(int, get_num_cols, setNumCols)
    showGrid = pyqtProperty(bool, get_show_grid, setShowGrid)
    rowMovingEnabled = pyqtProperty(bool, get_row_moving_enabled, setRowMovingEnabled)
    columnMovingEnabled = pyqtProperty(bool, get_column_moving_enabled, setColumnMovingEnabled)
    readOnly = pyqtProperty(bool, get_read_only, setReadOnly)
    sorting = pyqtProperty(bool, get_sorting, setSorting)
    selectionMode = pyqtProperty(SelectionModeEnum, get_selection_mode, setSelectionMode)
    focusStyle = pyqtProperty(FocusStyleEnum, get_focus_style, setFocusStyle)
    defaultRowHeight = pyqtProperty(int, get_default_row_height, setDefaultRowHeight)
    defaultColumnWidth = pyqtProperty(int, get_default_column_width, setDefaultColumnWidth)
    
    
    
        
    
    