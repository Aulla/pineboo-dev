# -*- coding: utf-8 -*-

from PyQt6 import QtGui, QtWidgets, QtCore

import os


class FLTableDB(QtWidgets.QWidget):

    te_search = None
    le_search = None
    te_in = None

    cb_1 = None
    cb_2 = None

    _table_name = None
    _foreign_field = None
    _field_relation = None
    _cc_enabled = False
    _cc_alias = None
    _find_hidden = None
    _filter_hidden = None
    _show_all_pixmap = None
    _function_get_color = None

    _layout_spacing = None
    _layout_marging = None

    _only_table = False
    _read_only = False
    _edit_only = False
    _insert_only = False
    _auto_sort_column = True

    readOnlyChanged = QtCore.pyqtSignal()
    insertOnlyChanged = QtCore.pyqtSignal()

    def __init__(self, parent):

        super().__init__(parent)

        self.layout_master = QtWidgets.QVBoxLayout()
        self.upper_layout = QtWidgets.QHBoxLayout()

        self.botton_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout = QtWidgets.QVBoxLayout()

        # Layout superior

        self.upper_frame = QtWidgets.QFrame(self)

        self.upper_layout.setSpacing(0)

        self.te_search = QtWidgets.QLabel(self)
        self.te_search.setText("Buscar")
        self.le_search = QtWidgets.QLineEdit(self)
        self.te_in = QtWidgets.QLabel(self)
        self.te_in.setText("en")

        self.cb_1 = QtWidgets.QComboBox(self)
        self.cb_2 = QtWidgets.QComboBox(self)

        # Layout inferior
        self.plain_text = QtWidgets.QPlainTextEdit(self)

        self.bt_table = QtWidgets.QPushButton(self)
        self.bt_filter = QtWidgets.QPushButton(self)
        self.bt_export = QtWidgets.QPushButton(self)
        self.bt_spacer = QtWidgets.QSpacerItem(
            0, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)

        self.bt_table.setIcon(
            QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.realpath(
                        os.path.join(os.path.dirname(__file__),
                                     "./icons/fltable-data.png")
                    )
                )
            )
        )
        self.bt_filter.setIcon(
            QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.realpath(
                        os.path.join(os.path.dirname(__file__),
                                     "./icons/fltable-filter.png")
                    )
                )
            )
        )
        self.bt_export.setIcon(
            QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.realpath(
                        os.path.join(os.path.dirname(__file__),
                                     "./icons/fltable-odf.png")
                    )
                )
            )
        )

        self.buttons_layout.addWidget(self.bt_table)
        self.buttons_layout.addWidget(self.bt_filter)
        self.buttons_layout.addWidget(self.bt_export)
        self.buttons_layout.addSpacerItem(self.bt_spacer)

        self.botton_layout.addWidget(self.plain_text)
        self.botton_layout.addLayout(self.buttons_layout)

        self.upper_layout.addWidget(self.te_search)
        self.upper_layout.addWidget(self.le_search)
        self.upper_layout.addWidget(self.te_in)
        self.upper_layout.addWidget(self.cb_1)
        self.upper_layout.addWidget(self.cb_2)

        self.upper_frame.setLayout(self.upper_layout)

        self.layout_master.addWidget(self.upper_frame)
        self.layout_master.addLayout(self.botton_layout)

        self.setLayout(self.layout_master)

        # Inicializamos !!

        self._table_name = ""
        self._foreign_field = ""
        self._field_relation = ""
        self._cc_enabled = False
        self._cc_alias = "Seleccionar"
        self._find_hidden = False
        self._filter_hidden = False
        self._show_all_pixmap = False

        self._layout_spacing = 0  # Default
        self._layout_marging = 0  # Default

        # self._function_get_color = ""

        self.update()

    def setTableName(self, tn):
        self._table_name = tn
        self.update()

    def setForeignField(self, ff):
        self._foreign_field = ff
        self.update()

    def setFieldRelation(self, fr):
        self._field_relation = fr
        self.update()

    def setCcEnabled(self, cce):
        self._cc_enabled = cce

    def setCcAlias(self, cca):
        self._cc_alias = cca

    def setFindHidden(self, b):
        self._find_hidden = b
        self.update()

    def setFilterHidden(self, b):
        self._filter_hidden = b
        self.update()

    def setShowAllPixmaps(self, b):
        self._show_all_pixmap = b

    def setFunctionGetColor(self, b):
        self._function_get_color = b

    def setOnlyTable(self, b):
        self._only_table = b

    def setReadOnly(self, b):
        self._read_only = b

    def setEditOnly(self, b):
        self._edit_only = b

    def setInsertOnly(self, b):
        self._insert_only = b

    def setAutoSortColumn(self, b):
        self._auto_sort_column = b

    def setLayoutSpacing(self, ls):
        self._layout_spacing = ls
        self.update()

    def setLayoutMarging(self, lm):
        self._layout_marging = lm
        self.update()

    def get_layout_marging(self):
        return self._layout_marging

    def get_layout_spacing(self):
        return self._layout_spacing

    def get_table_name(self):
        return self._table_name

    def get_foreign_field(self):
        return self._foreign_field

    def get_field_relation(self):
        return self._field_relation

    def get_cc_enabled(self):
        return self._cc_enabled

    def get_cc_alias(self):
        return self._cc_alias

    def get_find_hidden(self):
        return self._find_hidden

    def get_filter_hidden(self):
        return self._filter_hidden

    def get_show_all_pixmaps(self):
        return self._show_all_pixmap

    def get_funtion_get_color(self):
        return self._function_get_color

    def get_only_table(self):
        return self._only_table

    def get_read_only(self):
        return self._read_only

    def get_edit_only(self):
        return self._edit_only

    def get_insert_only(self):
        return self._insert_only

    def get_auto_sort_column(self):
        return self._auto_sort_column

    @QtCore.pyqtSlot()
    def insertRecord(self):
        pass

    @QtCore.pyqtSlot()
    def editRecord(self):
        pass

    @QtCore.pyqtSlot()
    def browseRecord(self):
        pass

    @QtCore.pyqtSlot()
    def deleteRecord(self):
        pass

    @QtCore.pyqtSlot()
    def copyRecord(self):
        pass

    def update(self):

        self.plain_text.clear()

        if len(self._table_name) > 0:
            self.plain_text.appendPlainText("tableName: %s" % self._table_name)
        if len(self._foreign_field) > 0:
            self.plain_text.appendPlainText(
                "foreignField: %s" % self._foreign_field)
        if len(self._field_relation) > 0:
            self.plain_text.appendPlainText(
                "fieldRelation: %s" % self._field_relation)

        if self._find_hidden:
            self.upper_frame.hide()
        else:
            self.upper_frame.show()

        if self._filter_hidden:
            self.bt_export.hide()
            self.bt_filter.hide()
            self.bt_table.hide()
        else:
            self.bt_export.show()
            self.bt_filter.show()
            self.bt_table.show()

        self.layout().setSpacing(self._layout_spacing)
        self.layout().setContentsMargins(self._layout_marging, 0, self._layout_marging, 0)

    tableName = QtCore.pyqtProperty(str, get_table_name, setTableName)
    foreignField = QtCore.pyqtProperty(str, get_foreign_field, setForeignField)
    fieldRelation = QtCore.pyqtProperty(
        str, get_field_relation, setFieldRelation)
    checkColumnEnabled = QtCore.pyqtProperty(
        bool, get_cc_enabled, setCcEnabled)
    aliasCheckColumn = QtCore.pyqtProperty(str, get_cc_alias, setCcAlias)
    findHidden = QtCore.pyqtProperty(bool, get_find_hidden, setFindHidden)
    filterHidden = QtCore.pyqtProperty(
        bool, get_filter_hidden, setFilterHidden)
    showAllPixmaps = QtCore.pyqtProperty(
        bool, get_show_all_pixmaps, setShowAllPixmaps)
    functionGetColor = QtCore.pyqtProperty(
        str, get_funtion_get_color, setFunctionGetColor)
    onlyTable = QtCore.pyqtProperty(bool, get_only_table, setOnlyTable)
    readOnly = QtCore.pyqtProperty(bool, get_read_only, setReadOnly)
    editOnly = QtCore.pyqtProperty(bool, get_edit_only, setEditOnly)
    insertOnly = QtCore.pyqtProperty(bool, get_insert_only, setInsertOnly)
    autoSortColumn = QtCore.pyqtProperty(
        bool, get_auto_sort_column, setAutoSortColumn)
    layoutSpacing = QtCore.pyqtProperty(
        int, get_layout_spacing, setLayoutSpacing)
    layoutMarging = QtCore.pyqtProperty(
        int, get_layout_marging, setLayoutMarging)
