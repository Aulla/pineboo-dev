# -*- coding: utf-8 -*-

from PyQt6 import QtGui, QtWidgets, QtCore
import enum
import os


class FLFieldDB(QtWidgets.QWidget):

    _label = None
    _editor = None
    _push_button = None

    _field_name = None
    _table_name = None
    _foreign_field = None
    _field_relation = None
    _field_alias = None
    _text_format = None
    _echo_mode = None

    _layout_spacing = None
    _layout_marging = None

    _show_alias = None
    _show_editor = None

    _auto_completion = None

    def __init__(self, parent=None):

        super().__init__(parent)
        lay = QtWidgets.QHBoxLayout()
        self._label = QtWidgets.QLabel(self)
        self._editor = QtWidgets.QLineEdit(self)
        self._editor.setMaximumHeight(22)
        self._push_button = QtWidgets.QPushButton(self)
        self._push_button.setIcon(
            QtGui.QIcon(
                QtGui.QPixmap(
                    os.path.realpath(
                        os.path.join(os.path.dirname(__file__),
                                     "../icons/flfielddb.png")
                    )
                )
            )
        )
        self._push_button.setMaximumSize(22, 22)
        self._push_button.setMinimumSize(22, 22)
        self._push_button.setFlat(True)

        lay.addWidget(self._label)
        lay.addWidget(self._push_button)
        lay.addWidget(self._editor)
        self.setLayout(lay)

        self._layout_spacing = 0  # Default
        self._layout_marging = 0  # Default

        self.fieldName = ""
        self._show_alias = True
        self._show_editor = True
        self._text_format = QtCore.Qt.TextFormat.AutoText  # (2) AutoText
        self._echo_mode = QtWidgets.QLineEdit.EchoMode.Normal  # normal
        self._auto_completion = 1  # OnDemandF4

        self.update()

    @QtCore.pyqtEnum
    class AutoCompletionEnum(enum.Enum):
        NeverAuto, OnDemandF4, AlwaysAuto = range(3)

    def setFieldName(self, f):
        self._field_name = f
        self._field_alias = f
        self.update()

    def get_field_name(self):
        return self._field_name

    def setTableName(self, t):
        self._table_name = t
        self.update()

    def get_table_name(self):
        return self._table_name

    def setForeignField(self, fr):
        self._foreign_field = fr
        self.update()

    def get_foreign_field(self):
        return self._foreign_field

    def setFieldRelation(self, fr):
        self._field_relation = fr
        self.update()

    def get_field_relation(self):
        return self._field_relation

    def setFieldAlias(self, fa):
        self._field_alias = fa
        self.update()

    def get_field_alias(self):
        return self._field_alias

    def setShowAlias(self, sa):
        self._show_alias = sa
        self.update()

    def get_show_alias(self):
        return self._show_alias

    def setShowEditor(self, se):

        self._show_editor = se
        self.update()

    def get_show_editor(self):
        return self._show_editor

    def get_text(self):
        return self._text_format

    def setText(self, t):
        self._text_format = t
        self.update()

    def get_echo_mode(self):
        return self._echo_mode

    def setEchoMode(self, m):
        self._echo_mode = m
        self.update()

    def get_layout_spacing(self):
        return self._layout_spacing

    def setLayoutSpacing(self, ls):
        self._layout_spacing = ls
        self.update()

    def get_layout_marging(self):
        return self._layout_marging

    def setLayoutMarging(self, lm):
        self._layout_marging = lm
        self.update()

    def get_auto_completion(self):
        return self._auto_completion

    def setAutoCompletion(self, ac):
        self._auto_completion = ac
        self.update()

    def update(self):
        value = ""
        if self._table_name not in ["", None]:
            value += "tN:%s," % self._table_name

        if self._foreign_field not in ["", None]:
            value += "fF:%s," % self._foreign_field

        if self._field_relation not in ["", None]:
            value += "fR:%s," % self._field_relation

        if self._field_alias in ["", None]:
            self._field_alias = "Error: fieldName vacio"

        self._label.setText(self._field_alias)

        self._editor.setText(value)

        if self._show_alias:
            self._label.show()
        else:
            self._label.hide()

        if self._show_editor:
            self._push_button.show()
            self._editor.show()
        else:
            self._push_button.hide()
            self._editor.hide()

        self.layout().setSpacing(self._layout_spacing)
        self.layout().setContentsMargins(self._layout_marging, 0, self._layout_marging, 0)
        self._label.setSizePolicy(self.sizePolicy())
        self._editor.setSizePolicy(self.sizePolicy())

    fieldName = QtCore.pyqtProperty(str, get_field_name, setFieldName)
    tableName = QtCore.pyqtProperty(str, get_table_name, setTableName)
    foreignField = QtCore.pyqtProperty(str, get_foreign_field, setForeignField)
    fieldRelation = QtCore.pyqtProperty(
        str, get_field_relation, setFieldRelation)
    fieldAlias = QtCore.pyqtProperty(str, get_field_alias, setFieldAlias)
    showAlias = QtCore.pyqtProperty(bool, get_show_alias, setShowAlias)
    showEditor = QtCore.pyqtProperty(bool, get_show_editor, setShowEditor)
    textFormat = QtCore.pyqtProperty(QtCore.Qt.TextFormat, get_text, setText)
    echoMode = QtCore.pyqtProperty(
        QtWidgets.QLineEdit.EchoMode, get_echo_mode, setEchoMode)
    layoutSpacing = QtCore.pyqtProperty(
        int, get_layout_spacing, setLayoutSpacing)
    layoutMarging = QtCore.pyqtProperty(
        int, get_layout_marging, setLayoutMarging)
    autoCompletionMode = QtCore.pyqtProperty(
        AutoCompletionEnum, get_auto_completion, setAutoCompletion)
